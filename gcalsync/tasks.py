from sync import Synchronizer

from celery.task import PeriodicTask
from celery.registry import tasks
from datetime import timedelta, datetime
from .models import SyncedCalendarGroup, SyncedCalendar

_tasks = []
_group_tasks = []


def run(calender_id, transformer):
    def func(self, **kwargs):
        synchronizer = Synchronizer(calendar_id=calender_id, 
            transformer=transformer)

        synchronizer.sync()

    return func


class TaskManager(object):
    def create_task(self, calendar_id, transformer):
        class_name = "CeleryTask_%s_%s" % (
            calendar_id, 
            type(transformer).__name__)
        return type(class_name, (PeriodicTask,), {
                "run_every": timedelta(seconds=120),
                "run": run(calendar_id, transformer)
            })

    def create_group_tasks(self, group_id, transformer):
        group = SyncedCalendarGroup.objects \
            .get_or_create(group_id=group_id)
        tasks_list = []
        for syncedcalendar in group.syncedcalendars:
            task = self.create_task(
                syncedcalendar.calendar_id,
                transformer)
            tasks_list.append(task)

        return tasks_list
        # class_name = "CeleryTask_%s_%s" % (
        #    group_id,
        #    type(transformer).__name__)
        # return type(class_name, (PeriodicTask,), {
        #    "run_every": timedelta(seconds=129),

    def setup_tasks(self, consumer_dict):
        global _tasks
        for calendar_id, transformers in consumer_dict.iteritems():
            for Transformer in transformers:
                _tasks.append(self.create_task(calendar_id, Transformer()))

        for Task in _tasks:
            tasks.register(Task)

    def setup_group_tasks(self, consumers_groups_dict):
        """
        Setup tasks to sync every calendar in the group
        """
        global _group_tasks
        for group_id, transformers in consumers_groups_dict.iteritems():
            for Transformer in transformers:
                _group_tasks = _group_tasks + \
                    self.create_group_tasks(
                        group_id, 
						Transformer())
        for Task in _group_tasks:
            tasks.register(Task)

	# TODO : RE-SETUP TASKS IF NEW CALENDAR IN A CERTAIN GROUP IS CREATED
