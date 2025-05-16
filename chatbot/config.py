import os
from google.colab import userdata
# Você pode manter a obtenção da chave do Colab para uso local, mas talvez queira suportar variáveis de ambiente também
GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY') or os.environ.get('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("Chave de API do Google não encontrada. Defina em GOOGLE_API_KEY no Colab ou como variável de ambiente.")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"