# Generated by Django 4.2.7 on 2023-11-22 13:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_remove_seumodelo_modelo_do_equipamento_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="seumodelo",
            name="escolha_principal",
        ),
        migrations.AddField(
            model_name="seumodelo",
            name="tipo_do_equipameto",
            field=models.CharField(
                choices=[
                    ("Smarthphone", "Celular"),
                    ("Desktop", "Computador"),
                    ("Notebook", "Notebook"),
                    ("Console", "Video Game"),
                ],
                default="Smarthphone",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="seumodelo",
            name="sub_escolha",
            field=models.CharField(
                choices=[
                    ("Oxidação", "Agua"),
                    ("Impacto", "Queda do chao"),
                    ("Marisia", "Cidade Litoranea"),
                    ("Mau uso", "Queda acidental"),
                    ("Tentaiva de reparo", "Mexeram antes"),
                ],
                default="Oxidação",
                max_length=20,
            ),
        ),
    ]
