# Generated by Django 3.1.11 on 2021-06-19 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0010_auto_20210619_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]