# views.py
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from ..models.loom import Loom
from ..serializers.loom import LoomSerializer
import csv



class LoomViewSet(viewsets.ModelViewSet):
    queryset = Loom.objects.all().order_by('-date')
    serializer_class = LoomSerializer


class LoomUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def get(self, request, *args, **kwargs):
        # Logic to handle GET request
        return Response({"message": "GET request received"}, status=status.HTTP_200_OK)

    print('parser_classes: ')

    def post(self, request, format=None):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            decoded_file = file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            looms = []

            for row in reader:
                serializer = LoomSerializer(data=row)
                if serializer.is_valid():
                    looms.append(Loom(**serializer.validated_data))
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            print('looms: ', looms[0])
            Loom.objects.bulk_create(looms)
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)