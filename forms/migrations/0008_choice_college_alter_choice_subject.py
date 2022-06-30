# Generated by Django 4.0.5 on 2022-06-30 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_rename_subject_choices_choice_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='college',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.mail'),
        ),
    ]
