# Generated by Django 3.2 on 2021-12-19 04:05

from django.db import migrations, models
import django_cpf_cnpj.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FullUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=50)),
                ('cpf', django_cpf_cnpj.fields.CPFField(max_length=14)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
