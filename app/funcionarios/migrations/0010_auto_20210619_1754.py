# Generated by Django 3.1.11 on 2021-06-19 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0009_auto_20210619_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
