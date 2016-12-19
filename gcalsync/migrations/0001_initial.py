# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SyncedCalendar',
            fields=[
                ('calendar_id', models.IntegerField(serialize=False, primary_key=True)),
                ('calendar_external_id', models.CharField(max_length=100)),
                ('last_synced', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SyncedCalendarGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_id', models.CharField(unique=True, max_length=100, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='SyncedEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('gcal_event_id', models.CharField(unique=True, max_length=100, db_index=True)),
                ('gcal_event_url', models.URLField(null=True, blank=True)),
                ('origin', models.CharField(default=b'google', max_length=6, choices=[(b'app', b'app'), (b'google', b'google')])),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('synced_calendar', models.ForeignKey(to='gcalsync.SyncedCalendar')),
            ],
        ),
        migrations.AddField(
            model_name='syncedcalendar',
            name='group',
            field=models.ForeignKey(related_name='syncedcalendars', to='gcalsync.SyncedCalendarGroup'),
        ),
    ]
