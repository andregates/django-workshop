# Generated by Django 3.2.5 on 2021-07-15 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0004_eventparticipant_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventparticipant',
            name='ip_address',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
