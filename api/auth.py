from pathlib import Path

import jwt
from cryptography.x509 import load_pem_x509_certificate


def decode_and_validate_token(access_token):
    unverified_headers = jwt.get_unverified_header(access_token)
    public_key = load_pem_x509_certificate(
        (Path(__file__).parent / "../public_key.pem").read_text().encode("utf-8")
    ).public_key()
    return jwt.decode(
        access_token,
        key=public_key,
        algorithms=unverified_headers["alg"],
        audience="http://127.0.0.1:8000/todo",
    )
