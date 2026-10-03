import warnings
import requests
from .exceptions import (
    RediroxError,
    RediroxConnectionError,
    RediroxAPIError,
    RediroxNotFoundError,
    RediroxAuthError,
    RediroxValidationError,
)

class Redirox:
    """Official Python client for Redirox URL Shortener.
    
    Example:
        >>> from redirox import Redirox
        >>> client = Redirox()
        >>> result = client.shorten("https://example.com")
        >>> print(result["short_url"])
    """

    def __init__(self, base_url="https://redirox.pages.dev", timeout=15):
        if "vercel.app" in base_url:
            warnings.warn(
                "The 'https://redirox.vercel.app' endpoint has moved to Cloudflare. "
                "Defaulting to 'https://redirox.pages.dev'. Please run 'pip install --upgrade redirox' "
                "or update your base_url.",
                UserWarning,
                stacklevel=2,
            )
            base_url = "https://redirox.pages.dev"
            
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _handle_response(self, response):
        """Parse response and raise helpful developer-friendly exceptions."""
        try:
            data = response.json()
        except Exception:
            data = {"error": response.text or f"HTTP {response.status_code}"}

        if response.status_code < 400:
            return data

        err_msg = data.get("error", f"Request failed with status {response.status_code}")

        if response.status_code == 400:
            raise RediroxValidationError(f"Invalid request: {err_msg}", status_code=400, response=data)
        elif response.status_code == 401:
            raise RediroxAuthError(f"Authentication failed: {err_msg}", status_code=401, response=data)
        elif response.status_code == 404:
            raise RediroxNotFoundError(f"Not found: {err_msg}", status_code=404, response=data)
        else:
            raise RediroxAPIError(f"Redirox API Error ({response.status_code}): {err_msg}", status_code=response.status_code, response=data)

    def shorten(
        self,
        url,
        password=None,
        expires_at=None,
        generate_qr=False,
    ):
        """Create a shortened URL with optional password, expiration, and QR code.
        
        Args:
            url (str): The destination URL (must start with http:// or https://).
            password (str, optional): Password to protect the short link.
            expires_at (str, optional): Expiration timestamp in ISO 8601 format.
            generate_qr (bool, optional): Whether to generate a base64 QR code image.
            
        Returns:
            dict: The created short link data containing 'code', 'short_url', etc.
        """
        if not url or not isinstance(url, str):
            raise RediroxValidationError("Parameter 'url' is required and must be a valid URL string.")

        if not (url.startswith("http://") or url.startswith("https://")):
            raise RediroxValidationError(f"Invalid URL format: '{url}'. URLs must start with 'http://' or 'https://'.")

        payload = {
            "url": url.strip(),
            "password": password.strip() if password else None,
            "expires_at": expires_at.strip() if expires_at else None,
            "generate_qr": bool(generate_qr),
        }

        try:
            response = requests.post(
                f"{self.base_url}/shorten",
                json=payload,
                timeout=self.timeout
            )
        except requests.exceptions.RequestException as e:
            raise RediroxConnectionError(
                f"Could not reach Redirox service at '{self.base_url}'. "
                f"Please check your internet connection or custom base_url. Details: {e}"
            ) from e

        return self._handle_response(response)

    def info(self, code):
        """Retrieve metadata, creation time, and total click analytics for a short link.
        
        Args:
            code (str): The short code (e.g. 'aB3x9z').
            
        Returns:
            dict: Link metadata containing 'code', 'url', 'visits', 'created_at', etc.
        """
        if not code or not isinstance(code, str):
            raise RediroxValidationError("Parameter 'code' is required (e.g. client.info('aB3x9z')).")

        code = code.strip().split("/")[-1]

        try:
            response = requests.get(
                f"{self.base_url}/info/{code}",
                timeout=self.timeout
            )
        except requests.exceptions.RequestException as e:
            raise RediroxConnectionError(
                f"Could not reach Redirox service at '{self.base_url}'. Details: {e}"
            ) from e

        return self._handle_response(response)

    def verify(self, code, password):
        """Verify the password for a protected short link.
        
        Args:
            code (str): The short code.
            password (str): The password to verify.
            
        Returns:
            dict: {'success': True} if valid.
            
        Raises:
            RediroxAuthError: If the password is incorrect.
            RediroxNotFoundError: If the link does not exist.
        """
        if not code or not isinstance(code, str):
            raise RediroxValidationError("Parameter 'code' is required.")
        if not password:
            raise RediroxValidationError("Parameter 'password' is required.")

        code = code.strip().split("/")[-1]

        try:
            response = requests.post(
                f"{self.base_url}/verify/{code}",
                json={"password": password.strip()},
                timeout=self.timeout
            )
        except requests.exceptions.RequestException as e:
            raise RediroxConnectionError(
                f"Could not reach Redirox service at '{self.base_url}'. Details: {e}"
            ) from e

        return self._handle_response(response)
