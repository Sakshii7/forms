# Generated by Django 4.0.5 on 2022-06-30 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
