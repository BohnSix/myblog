import os
from app import create_app
from dotenv import load_dotenv

dotev_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotev_path):
    load_dotenv(dotev_path)

app = create_app("product")
