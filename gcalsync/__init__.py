from registry import Register
from discovery import ConsumerManager
from tasks import TaskManager

_consumer_manager = ConsumerManager()
_task_manager = TaskManager()
_register = Register()

# Add a user or a local calendar
def register(calendar_id, transformers):
    _register.register(calendar_id, transformers)

def register_group(calendar_group_id, transformers):
    _register.register_group(calendar_group_id, transformers)

_consumer_manager.autodiscover()
_task_manager.setup_tasks(_register.consumers)
_task_manager.setup_group_tasks(_register.consumers_groups)
