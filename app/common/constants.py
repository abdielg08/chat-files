import os, chromadb
from chromadb.config import Settings

# Define the folder for storing database
#PERSIST_DIRECTORY = os.environ.get('PERSIST_DIRECTORY', 'db')

# Define the Chroma settings
CHROMA_SETTINGS = chromadb.HttpClient(host="https://chroma-602716772659.us-central1.run.app", port=8000, settings=Settings(allow_reset=True, anonymized_telemetry=False))
