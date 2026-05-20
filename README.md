# Redirox

<p align="center">
  <img src="https://redirox.vercel.app/redirox.png" width="120" alt="Redirox Logo">
</p>

<h3 align="center">🚀 Smart Links. Clean Routes.</h3>

<p align="center">
  Official Python SDK for Redirox URL Shortener
</p>

<p align="center">
  <a href="https://pypi.org/project/redirox/">
    <img src="https://img.shields.io/pypi/v/redirox?color=blue" alt="PyPI">
  </a>

  <a href="https://pypi.org/project/redirox/">
    <img src="https://img.shields.io/pypi/pyversions/redirox" alt="Python Versions">
  </a>

  <a href="https://github.com/lib-kishore/redirox/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/lib-kishore/redirox" alt="License">
  </a>
</p>

---

## 🌐 About

I recently created Redirox, a lightweight and modern URL shortener.  
I always wondered:

> “Is building a clean URL shortener actually simple?”

So I built Redirox with one goal in mind:

- Lightweight
- Fast
- Modern
- Developer friendly

🔗 Website: https://redirox.vercel.app

Since I had already created Python packages before, I thought:

> “Why not create a PyPI package for Redirox too?”

Now developers can shorten links, generate QR codes, and manage expiring URLs directly from Python.

---

## ✨ Features

- Short link generation
- Password-protected links
- Expiration date support
- QR code generation
- Fast redirects
- Simple API
- Lightweight SDK
- Clean developer experience

---

## 📦 Installation

```bash
pip install redirox
```

---

## ⚡ Quick Start

```python
from redirox import Redirox

client = Redirox()

result = client.shorten(
    "https://google.com"
)

print(result)
```

---

## 🔗 Shorten a URL

```python
from redirox import Redirox

client = Redirox()

result = client.shorten(
    "https://example.com"
)

print("Short URL:", result["short_url"])
```

---

## 📱 Generate QR Codes

```python
from redirox import Redirox

client = Redirox()

result = client.shorten(
    "https://github.com",
    generate_qr=True
)

print(result["qr_code"])
```

---

## 💾 Save QR Code as PNG

The QR code is returned as a base64 encoded PNG image.

```python
import base64

qr_data = result["qr_code"].split(",")[1]

with open("qr.png", "wb") as f:
    f.write(base64.b64decode(qr_data))

print("QR code saved!")
```

---

## 🔒 Password Protected Links

```python
from redirox import Redirox

client = Redirox()

result = client.shorten(
    "https://example.com",
    password="mypassword"
)

print(result)
```

---

## ⏳ Expiring Links

```python
from redirox import Redirox
from datetime import datetime, timedelta

client = Redirox()

expires_at = (
    datetime.utcnow() + timedelta(hours=1)
).isoformat()

result = client.shorten(
    "https://example.com",
    expires_at=expires_at
)

print(result["expires_at"])
```

---

## 📊 Get Link Information

```python
from redirox import Redirox

client = Redirox()

info = client.info("abc123")

print(info)
```

---

## 📄 Example Response

```python
{
    "code": "abc123",
    "short_url": "https://redirox.vercel.app/abc123",
    "url": "https://google.com",
    "qr_code": None,
    "expires_at": None,
    "has_password": False
}
```

---

## 🎯 Philosophy

Redirox focuses on simplicity.

No bloated dashboards.  
No forced accounts.  
No unnecessary friction.

Just fast redirects, clean APIs, and modern workflows.

---

## 🌍 Open Source

Contributions are welcome!

Whether it's:
- Fixing bugs
- Improving documentation
- Suggesting features
- Enhancing the SDK

Feel free to open issues or submit pull requests.

---

## 🔗 Links

- Website: https://redirox.vercel.app
- PyPI: https://pypi.org/project/redirox/
- GitHub: https://github.com/lib-kishore/redirox

---

## 📄 License

MIT License © Kishore

---

<p align="center">
  ❤️ Made with passion by Kishore
</p>
