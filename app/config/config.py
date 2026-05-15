# FIXME: DEPRECATED, ONLY KEEPING THIS FOR LOGGING PURPOSES FOR NOW

import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    # Config
    command_prefix: str = '$'
    permissions_integer: int = os.getenv('2815128261348544')

    # .env
    app_id: int = os.getenv('APP_ID')
    public_key: str = os.getenv('PUBLIC_KEY')
    token: str = os.getenv('TOKEN')
    client_secret: str = os.getenv('CLIENT_SECRET')