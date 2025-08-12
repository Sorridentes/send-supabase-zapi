import logging
from src.database.supabase_client import SupabaseClient
from src.services.zapi_service import ZAPIService
from src.config import settings

# Configuração basica de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def main():
    logger.info("Iniciando o processo de envio de mensagens")

    try:
        # Recebe contatos do Supabase
        db_client = SupabaseClient()
        contacts = db_client.get_contacts()

        if not contacts:
            logger.warning("Nenhum contato encontrado no database")
            return
        
        # Processa cada contato
        for contact in contacts:
            phone = contact.get('phone')
            name = contact.get('name', 'Amigo')

            if not phone:
                logger.warning(f"Contato saltado - faltando número de telefone: {contact}")
                continue

            # Mensagem personalizada
            message = f"Olá {name}, tudo bem com você?"
            logger.info(f"Preparando para enviar mensagem para {phone}")

            # Envia mensage via Z-API
            ZAPIService.send_message(phone, message)

    except Exception as e:
        logger.error(f"Erro critico no processo da main: {str(e)}")
        raise

    logger.info("Processo de envio de mensagens completo")

if __name__ == "__main__":
    main()