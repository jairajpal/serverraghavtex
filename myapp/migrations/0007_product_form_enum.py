# Generated by Django 5.1 on 2024-08-27 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_product_quality_alter_product_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='form_enum',
            field=models.CharField(choices=[('raw', 'Raw'), ('dispatch', 'Dispatch')], default='raw', max_length=50),
        ),
    ]
