# Generated by Django 2.2rc1 on 2019-07-15 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0004_auto_20190714_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='name',
        ),
    ]
