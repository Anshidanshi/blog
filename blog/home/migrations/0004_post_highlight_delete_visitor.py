# Generated by Django 4.2.1 on 2023-07-02 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_breakingnew'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='highlight',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Visitor',
        ),
    ]
