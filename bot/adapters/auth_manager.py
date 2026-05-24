import hashlib
import hmac

def generate_cid(user_handle: str, platform: str, secret_key: bytes) -> str:
    """Generates a secure, deterministic CID using HMAC-SHA256."""
    message = f"{user_handle}:{platform}".encode()
    signature = hmac.new(secret_key, message, hashlib.sha256).hexdigest()
    return signature[:16] # Truncated for usability
