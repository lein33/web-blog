# Generated by Django 4.2 on 2023-05-04 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manual',
            name='Tags',
            field=models.ManyToManyField(to='proyectos.tag', verbose_name='etiquetas'),
        ),
    ]