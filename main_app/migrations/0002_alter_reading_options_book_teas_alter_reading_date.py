# Generated by Django 4.1.4 on 2022-12-21 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reading',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='book',
            name='teas',
            field=models.ManyToManyField(to='main_app.tea'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='date',
            field=models.DateField(verbose_name='reading date'),
        ),
    ]