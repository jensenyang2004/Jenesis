# Generated by Django 5.0.7 on 2024-07-17 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_customsinfo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customsinfo",
            name="gmail",
            field=models.EmailField(max_length=254),
        ),
    ]
