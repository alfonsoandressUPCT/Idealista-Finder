import requests
import base64
import os
from dotenv import load_dotenv
import time

# Cargar variables de entorno
load_dotenv()

class IdealistaAPI:

    def __init__(self):
        self.api_key = os.getenv('IDEALISTA_API_KEY')
        self.secret = os.getenv('IDEALISTA_SECRET')
        self.auth_token = None
        self.token_expires = 0
        self.base_url = 'https://api.idealista.com/3.5'
    
    def authenticate(self):
        """Obtiene un token de autenticación OAuth2"""
        if self.auth_token and time.time() < self.token_expires: # Si el token aún es válido, no lo volvemos a solicitar
            return
            
        # Preparar credenciales en formato "api_key:secret" codificado en base64
        credentials = f"{self.api_key}:{self.secret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        
        # Configurar cabeceras y datos para la solicitud de token
        headers = {
            'Authorization': f'Basic {encoded_credentials}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        # Datos para la solicitud de token
        data = {
            'grant_type': 'client_credentials',
            'scope': 'read'
        }
        
        # Realizar la petición para obtener el token
        response = requests.post(
            'https://api.idealista.com/oauth/token',
            headers=headers,
            data=data
        )
        
        if response.status_code == 200:
            token_data = response.json() # Parsear la respuesta JSON
            self.auth_token = token_data['access_token'] # Guardar el token de acceso

            # Guardar cuándo expira el token (restamos 60 segundos por seguridad)
            self.token_expires = time.time() + token_data['expires_in'] - 60
        else:
            raise Exception("Error al obtener el token de autenticación: " + response.text)
    
    def search_properties(self, params):
        """Busca propiedades según los parámetros especificados"""
        self.authenticate()
        
        headers = {
            'Authorization': f'Bearer {self.auth_token}'
            # No incluimos Content-Type, requests lo establecerá automáticamente para multipart/form-data
        }
        
        # Realizar la búsqueda usando multipart/form-data
        response = requests.post(
            f'{self.base_url}/es/search',
            headers=headers,
            data=params  # Enviamos los parámetros como datos de formulario, no como JSON
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error en la búsqueda: {response.status_code}")