# Generated by Django 4.1 on 2024-05-19 13:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cinema", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="image",
            field=models.ImageField(null=True, upload_to="333"),
        ),
    ]
