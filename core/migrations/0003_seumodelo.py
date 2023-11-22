# Generated by Django 4.2.7 on 2023-11-21 17:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_ordem_remove_cidade_parte_cidade_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="SeuModelo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "tipo_de_equipamento",
                    models.CharField(
                        choices=[
                            ("SmartPhone", "Celular"),
                            ("PC", "Desktop"),
                            ("PC", "Notebook"),
                            ("Console", "Video Game"),
                        ],
                        max_length=20,
                    ),
                ),
                ("modelo_do_equipamento", models.CharField(choices=[], max_length=255)),
            ],
        ),
    ]
