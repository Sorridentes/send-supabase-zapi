from supabase import create_client, Client
from src.config import settings
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)

class SupabaseClient:
    def __init__(self):
        self.client: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
        logger.info("Inicilização do cliente Supabase")

    def get_contacts(self, limit:int=3) -> List[Dict]:
        # Coleta contatos do Supabase com tratamento de erros
        try:
            response = self.client.table('contacts').select('*').limit(limit).execute()
            logger.info(f"Coletatos {len(response.data)} contatos do Supabase")
            return response.data
        except Exception as e:
            logger.error(f"Erro ao buscar contatos: {str(e)}")
            raise