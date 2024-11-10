import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")