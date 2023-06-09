# Generated by Django 4.1.5 on 2023-02-26 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('owner', models.CharField(max_length=200)),
                ('km_driven', models.PositiveIntegerField()),
                ('purchased_date', models.DateField(null=True)),
                ('fuel_type', models.CharField(choices=[('petrol', 'petrol'), ('diesel', 'diesel'), ('ev', 'ev')], max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('vehicle_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
