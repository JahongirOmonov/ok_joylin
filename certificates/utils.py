import qrcode
from django.conf import settings
from pathlib import Path

def generate_qr(uuid):
    qr_dir = Path(settings.BASE_DIR) / 'media/qr'
    qr_dir.mkdir(parents=True, exist_ok=True)

    qr_path = qr_dir / f"{uuid}.png"

    url = f"http://127.0.0.1:8000/certificates/verify/{uuid}/"

    img = qrcode.make(url)
    img.save(qr_path)

    return f"qr/{uuid}.png"
