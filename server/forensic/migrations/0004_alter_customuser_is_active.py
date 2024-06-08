# Generated by Django 5.0.6 on 2024-06-08 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forensic', '0003_alter_customuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]
