class EnvironmentException(Exception):
    def __init__(self, message: str, cause: Exception | None = None):
        self._message = message
        self._cause = cause

    @property
    def message(self) -> str:
        return self._message

    @property
    def cause(self) -> Exception | None:
        return self._cause

class ApiClientException(Exception):
    """Raise this exception upon errors with API client wrappers."""
    def __init__(self, message: str, cause: Exception | None = None):
        self._message = message
        self._cause = cause

    @property
    def message(self) -> str:
        return self._message

    @property
    def cause(self) -> Exception | None:
        return self._cause
