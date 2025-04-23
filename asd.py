import requests
from dotenv import load_dotenv
import os
from typing import Tuple, Optional


class EnvironmentConfig:
    """Maneja la carga y validación de las variables de entorno.."""
    
    @staticmethod
    def load_environment_variables() -> Tuple[str, str]:
        """Carga y valida las variables de entorno requeridas.
        
        Returns:
            Tupla que contiene la clave API y el Engine ID
            
        Raises:
            ValueError: Si faltan las variables de entorno requeridas.
        """
        load_dotenv()
        api_key = os.getenv("API_KEY")
        search_engine_id = os.getenv("ENGINE_ID")

        if not api_key:
            raise ValueError("API_KEY not found in environment variables")
        if not search_engine_id:
            raise ValueError("ENGINE_ID not found in environment variables")

        return api_key, search_engine_id


class GoogleSearchAPI:
    """maneja las interacciones con la Google Custom Search API."""
    
    def __init__(self, api_key: str, search_engine_id: str):
        """Iniciar api con credenciales"""
        self.api_key = api_key
        self.search_engine_id = search_engine_id
        self.base_url = "https://www.googleapis.com/customsearch/v1"
        
    def build_search_url(self, query: str, page: int = 1, language: str = "lang_es") -> str:
        """Construct the API request URL with parameters."""
        return (f"{self.base_url}?key={self.api_key}&cx={self.search_engine_id}"
                f"&q={query}&start={page}&lr={language}")
    
    def execute_search(self, query: str) -> Optional[dict]:
        """Ejecuta una busqueda en la query de la API de google.
        
        Args:
            query: la search query string
            
        Returns:
            JSON response data si es correcto, none si no
            
        Raises:
            ValueError: Si la api falla
        """
        url = self.build_search_url(query)
        response = requests.get(url)
        
        if not response.ok:
            raise ValueError(f"API request failed with status {response.status_code}")
            
        return response.json()


def main():

    try:
        # carga y valida la configuracion
        api_key, search_engine_id = EnvironmentConfig.load_environment_variables()
        print(f"Loaded configuration: API_KEY={api_key[:4]}..., ENGINE_ID={search_engine_id[:4]}...")
        
        # Inicia el cliente API
        search_client = GoogleSearchAPI(api_key, search_engine_id)
        
        # ejecuta busqueda
        search_query = 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'
        search_results = search_client.execute_search(search_query)
        
        # Resultados del proceso 
        print(f"Search results: {search_results}")
        
    except ValueError as error:
        print(f"Error: {error}")
    except requests.RequestException as error:
        print(f"Network error occurred: {error}")


if __name__ == "__main__":
    main()