import requests
from src.config import settings
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class ZAPIService:
    BASE_URL: str = settings.ZAPI_BASE_URL

    @classmethod
    def send_message(cls, phone: str, message: str) -> Optional[dict]:
        # Envia uma mensagem via Z-API com tratamento de erros
        url: str = cls.BASE_URL

        payload = {
            "phone": phone,
            "message": message
        }

        headers = {
            "Client-Token": settings.ZAPI_TOKEN
        }

        try:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            response.raise_for_status() # Verifica se houve erro na requisição
            logger.info(f"Messagem enviada para {phone} - Status: {response.status_code}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f'Falha ao enviar mensagem para {phone}: {str(e)}')
            return None