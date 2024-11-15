# Generated by Django 5.1.3 on 2024-11-15 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('ProfesorID', models.AutoField(primary_key=True, serialize=False)),
                ('Nume', models.CharField(max_length=100)),
                ('Prenume', models.CharField(max_length=100)),
                ('DataNasterii', models.DateField()),
                ('Specializare', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Telefon', models.CharField(max_length=15)),
                ('DataAngajarii', models.DateField()),
            ],
            options={
                'db_table': 'Profesor',
            },
        ),
    ]
