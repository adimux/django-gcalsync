from oauth2client.file import Storage

class CredentialsException(Exception):
    pass

class CredentialsProvider(object):
    
    def get_credentials(cls, context):
        """
        Parameters
        ----------
        context dict
            A dictionary containing informaions about the context from within we want to connect to the remote calendar.
            Contains minimally "synced_calendar", "transformer", etc.
        """
        raise NotImplementedError("BaseCredentialsProvider subclass must implement get_credentials() method")

class FileCredentialsProvider(CredentialsProvider):

    def get_credentials(cls, context):
        storage = Storage(settings.GCALSYNC_CREDENTIALS)
        credentials = storage.get()

        return credentials


def get_credentials_provider():
    provider_class = None

    if hasattr(settings, "CREDENTIALS_PROVIDER"):
        try:
            provider_class_temp = import_class(
                settings.CREDENTIALS_PROVIDER)
            provider_class = provider_class_temp
        except ImportError:
            raise RuntimeError("Could not import Credentials Provider %s " % settings.CREDENTIAL_PROVIDER)
        else:
            raise ImproperlyConfigured("CREDENTIALS_PROVIDER constant not found in settings. Please provide it with a value of a classpath to a provider")
        return provider_class()
