# Generated by Django 2.2rc1 on 2019-07-14 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.CharField(default='arun', max_length=50),
            preserve_default=False,
        ),
    ]
