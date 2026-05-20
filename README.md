# Routly (PyPI)

## 🚀 Smart Links. Clean Routes.

I recently created Routly, a link shortener website.  
I always wondered: "Is creating a URL shortener actually simple?"  

So I built Routly with one goal in mind: keep it lightweight, modern, and clean.  
The website is live at: https://routly-test.vercel.app  

Since I had already created a Python package before, I thought:  
"Why not make a PyPI package for Routly too?"  

This way, developers can shorten links, set expiration dates, and download QR codes directly from Python.

---

## ✨ Features

- Short link generation
- Password-protected links
- Expiration dates (validated to always be in the future)
- QR code generation and download
- Easy copy & sharing
- Fast redirects
- Clean and modern design

---

## 📦 Installation

```
pip install routly
```

---

## 🐍 Usage

### Shorten a URL

```python
from routly.client import RoutlyClient

client = RoutlyClient()

result = client.shorten("https://example.com", generate_qr=True)

print("Short URL:", result["short_url"])
print("QR Code (base64):", result["qr_code"])
```

---

### Download QR Code as Image

The API returns the QR code as a base64-encoded PNG. You can save it locally:

```python
import base64

qr_data = result["qr_code"].split(",")[1]  # remove "data:image/png;base64,"
with open("qr.png", "wb") as f:
    f.write(base64.b64decode(qr_data))

print("QR code saved as qr.png")
```

---

### Set Expiration Date and Time

Expiration must always be in the future — past dates are rejected (just like in the JS frontend).

```python
from datetime import datetime, timedelta

# Example: expire in 1 hour
expires_at = (datetime.utcnow() + timedelta(hours=1)).isoformat()

result = client.shorten("https://example.com", expires_at=expires_at)

print("Expires at:", result["expires_at"])
```

---

### Error Handling

The client raises exceptions for common errors:

```python
from routly.client import RoutlyClient
from routly.exceptions import ValidationError, ServerError, RoutlyError

client = RoutlyClient()

try:
    result = client.shorten("invalid-url")
except ValidationError as e:
    print("Validation failed:", e)
except ServerError:
    print("Server error, try again later.")
except RoutlyError as e:
    print("Unexpected error:", e)
```

---

## 🎯 Philosophy

Routly focuses on simplicity.  
No bloated dashboards, forced accounts, or unnecessary friction — just clean workflows, fast experience, and essential functionality.

---

## 🌍 Open Source

Contributions are welcome!  
Whether it’s fixing bugs, improving documentation, or suggesting features — feel free to open issues or submit pull requests.

---

## 📄 License

MIT License © Kishore

---

### ❤️ Made with passion by Kishore

---
