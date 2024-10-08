# Generated by Django 5.1 on 2024-10-06 04:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bname', models.CharField(max_length=255)),
                ('bisbn', models.IntegerField()),
                ('bookid', models.IntegerField(primary_key=True, serialize=False)),
                ('bookcategory', models.CharField(max_length=255)),
                ('bookstatus', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('registrationno', models.IntegerField(primary_key=True, serialize=False)),
                ('bankaccount', models.IntegerField()),
                ('cnic', models.IntegerField()),
                ('phoneno', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('bookid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='firstapp.book')),
            ],
        ),
        migrations.CreateModel(
            name='BookPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.IntegerField()),
                ('bookid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='firstapp.book')),
            ],
        ),
        migrations.CreateModel(
            name='Fine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fineID', models.IntegerField()),
                ('Amount', models.IntegerField()),
                ('registration', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='firstapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='BookIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('bookid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='firstapp.book')),
                ('registration', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='firstapp.user')),
            ],
        ),
    ]
