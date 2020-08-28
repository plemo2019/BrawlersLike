# Generated by Django 3.0.8 on 2020-08-28 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='skin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('Description', models.CharField(max_length=500)),
                ('Avatar', models.URLField(max_length=500)),
                ('Price', models.IntegerField()),
                ('Model3DFile', models.URLField(max_length=500)),
                ('TextureFile', models.URLField(max_length=500)),
                ('VoiceLineFile', models.URLField(max_length=500)),
            ],
        ),
    ]
