import requests

class Redirox:
    def __init__(self, base_url="https://redirox.vercel.app"):
        self.base_url = base_url.rstrip("/")

    def shorten(
        self,
        url,
        password=None,
        expires_at=None,
        generate_qr=False,
    ):
        payload = {
            "url": url,
            "password": password,
            "expires_at": expires_at,
            "generate_qr": generate_qr,
        }

        response = requests.post(
            f"{self.base_url}/shorten",
            json=payload
        )

        response.raise_for_status()
        return response.json()

    def info(self, code):
        response = requests.get(
            f"{self.base_url}/info/{code}"
        )

        response.raise_for_status()
        return response.json()
