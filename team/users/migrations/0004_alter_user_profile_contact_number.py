# Generated by Django 5.0.1 on 2024-02-19 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='contact_number',
            field=models.CharField(default='9999999990', max_length=20, unique=True),
        ),
    ]
