# Base64-encoded AWS-like key

import base64

encoded_key = "QUtJQUlPU0ZPRE5ON0VYQU1QTEU="
decoded = base64.b64decode(encoded_key).decode()
