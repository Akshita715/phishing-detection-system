# Phishing Detection System

## Project Overview

This project detects phishing attempts by analyzing URLs and email text.

It identifies suspicious keywords, unusual URL patterns, fake domains, and other phishing indicators.

---

## Features

- URL Analysis
- Email Analysis
- Keyword Detection
- HTTP/HTTPS Detection
- IP Address Detection
- Long URL Detection
- Shortened URL Detection
- Safe / Suspicious Classification

---

## Technologies

- Python
- Flask
- HTML
- CSS

---

## How to Run

Create virtual environment

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Install packages

```bash
pip install -r requirements.txt
```

Run

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## Example

Input

```
http://paypal-login-secure.com/verify
```

Output

```
Status : Suspicious

Reasons

- HTTP
- login keyword
- verify keyword
- secure keyword
- hyphen
```