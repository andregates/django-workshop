# Generated by Django 3.2.5 on 2021-08-15 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0009_remove_eventparticipant_knowledge_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventparticipant',
            name='knowledge_level',
            field=models.CharField(choices=[('0', 'Desconhece'), ('1', 'Básico'), ('2', 'Intermediário'), ('3', 'Avançado')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]