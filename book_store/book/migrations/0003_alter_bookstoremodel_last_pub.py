# Generated by Django 5.0.6 on 2024-06-28 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_bookstoremodel_last_pub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstoremodel',
            name='last_pub',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
