# Generated by Django 4.1.4 on 2022-12-21 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_book_rating_alter_tea_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tea',
            name='rating',
            field=models.IntegerField(),
        ),
    ]