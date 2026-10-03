class RediroxError(Exception):
    """Base exception for all Redirox SDK errors."""
    pass

class RediroxConnectionError(RediroxError):
    """Raised when unable to connect to the Redirox service."""
    pass

class RediroxAPIError(RediroxError):
    """Raised when the Redirox API returns an error response."""
    def __init__(self, message, status_code=None, response=None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response

class RediroxNotFoundError(RediroxAPIError):
    """Raised when a short code does not exist or has expired (404)."""
    pass

class RediroxAuthError(RediroxAPIError):
    """Raised when password authentication fails for a protected link (401)."""
    pass

class RediroxValidationError(RediroxAPIError):
    """Raised when invalid arguments or URLs are provided (400)."""
    pass
