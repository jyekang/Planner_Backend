# Generated by Django 4.2.3 on 2023-07-27 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_expense'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('rsvp', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['rsvp', 'full_name'],
            },
        ),
    ]