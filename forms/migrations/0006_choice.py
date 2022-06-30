# Generated by Django 4.0.5 on 2022-06-30 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_mail_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_choices', models.ForeignKey(choices=[('sci', 'SCIENCE'), ('math', 'MATHS'), ('phy', 'PHYSICS'), ('chem', 'CHEMISTRY')], default='sci', on_delete=django.db.models.deletion.CASCADE, to='forms.mail')),
            ],
        ),
    ]
