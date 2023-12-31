# Generated by Django 4.2.3 on 2023-07-31 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_event'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendee',
            options={},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.AddField(
            model_name='event',
            name='attendee_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to='planner.attendee'),
        ),
    ]
