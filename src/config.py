import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Settings(BaseModel):
    SUPABASE_URL: str = os.getenv("SUPABASE_URL")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")
    ZAPI_TOKEN: str = os.getenv("ZAPI_TOKEN")
    ZAPI_INSTANCE: str = os.getenv("ZAPI_INSTANCE")

    class Config:
        env_file= '.env'

settings = Settings()