# Generated by Django 4.0.6 on 2022-08-04 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_rename_count_postcounter_countid'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcounter',
            name='slug',
            field=models.SlugField(max_length=250, null=True),
        ),
    ]
