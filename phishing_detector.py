import re
from urllib.parse import urlparse

KEYWORDS = [
    "login",
    "verify",
    "password",
    "bank",
    "secure",
    "account",
    "otp",
    "urgent",
    "update",
    "confirm",
    "click",
    "gift",
    "winner",
    "free"
]

SHORTENERS = [
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "goo.gl"
]


def analyze_input(text):

    score = 0
    reasons = []

    text = text.strip()

    if len(text) > 75:
        score += 1
        reasons.append("Long URL detected")

    if text.startswith("http://"):
        score += 1
        reasons.append("HTTP is less secure than HTTPS")

    if "@" in text:
        score += 2
        reasons.append("@ symbol detected")

    ip_pattern = r"\d+\.\d+\.\d+\.\d+"

    if re.search(ip_pattern, text):
        score += 2
        reasons.append("IP Address detected")

    try:
        domain = urlparse(text).netloc

        if "-" in domain:
            score += 1
            reasons.append("Hyphen in domain")

    except:
        pass

    for word in KEYWORDS:
        if word in text.lower():
            score += 1
            reasons.append(f"Keyword found : {word}")

    for site in SHORTENERS:
        if site in text.lower():
            score += 2
            reasons.append(f"Shortened URL : {site}")

    if score <= 2:
        status = "🟢 SAFE"

    elif score <= 5:
        status = "🟠 MEDIUM RISK"

    else:
        status = "🔴 SUSPICIOUS"

    return {
        "status": status,
        "score": score,
        "reasons": reasons
    }