# Generated by Django 3.0.8 on 2020-09-03 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gis_map', '0002_auto_20200803_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputloc',
            name='search_choice',
            field=models.CharField(choices=[('ES', 'Expanding Square'), ('PS', 'Parallel Sweep'), ('CS', 'Creeping Sweep')], default='ES', help_text='Choose the search route to display on map', max_length=30),
        ),
    ]
