import httplib2
from oauth2client.file import Storage
from django.conf import settings
import importlib
from apiclient.discovery import build
from gcalsync.utils import import_class
from django.core.exceptions import ImproperlyConfigured
from .credentials import CredentialsProvider
from .credentials import get_credentials_provider


class Connection(object):
    service = None

    def __init__(self, context=None):
        super(Connection, self).__init__()
        self.context = context

    def get_credentials(self, context=None):
        if context is None:
            context = self.context
            if context is None:
                raise ValueError(
                    "When getting credentials, you need "
                    + "either to give context at instantiating"
                    + "Connection object or passing the "
                    + "context when calling get_credentials() method.")

        return get_credentials_provider() \
            .get_credentials(context)

    def get_service(self, context=None):
        if self.service:
            return self.service

        else:
            credentials = self.get_credentials(context=context)

            http = httplib2.Http()
            http = credentials.authorize(http)

            self.service = build(serviceName='calendar', version='v3', http=http,
                 developerKey=settings.GCALSYNC_APIKEY)

            return self.service
