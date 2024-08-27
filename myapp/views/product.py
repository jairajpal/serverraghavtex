from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from ..models.product import Product
from ..serializers.product import ProductSerializer
import csv

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-date')  # Ensure this is properly defined
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()  # Start with the base queryset

        form_enum = self.request.query_params.get('form_enum', None)
        print('form_enum: ', form_enum)
        if form_enum:
            if form_enum == 'raw':
                queryset = queryset.filter(form_enum='raw')  # Adjust as needed
            elif form_enum == 'dispatch':
                queryset = queryset.filter(form_enum='dispatch')  # Adjust as needed

        return queryset

class ProductUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            decoded_file = file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            products = []

            for row in reader:
                serializer = ProductSerializer(data=row)
                if serializer.is_valid():
                    products.append(Product(**serializer.validated_data))
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            print('products: ', products[0])
            Product.objects.bulk_create(products)
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)