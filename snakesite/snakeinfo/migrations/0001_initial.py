# Generated by Django 2.1.1 on 2018-10-17 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('avg_lifespan_years', models.IntegerField()),
                ('skill_level', models.CharField(max_length=50)),
                ('temp_requirement', models.CharField(max_length=50)),
            ],
        ),
    ]
