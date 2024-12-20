# Generated by Django 5.0.2 on 2024-12-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('property_type', models.CharField(choices=[('Residential', 'Residential'), ('Commercial', 'Commercial'), ('Villa', 'Villa')], max_length=50)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Sold', 'Sold')], max_length=20)),
            ],
        ),
    ]
