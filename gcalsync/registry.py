
class Register(object):
    def __init__(self):
        self.consumers = {}
        self.consumers_groups = {}
    
    def register(self, calendar_id, transformers):
        if not calendar_id in self.consumers:
            self.consumers[calendar_id] = transformers

    def register_group(self, group_id, transfomers):
        if not group_id in self.consumers_groups:
            self.consumers_groups[group_id] = transformers
            
