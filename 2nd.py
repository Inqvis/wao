from dotenv import load_dotenv
import os
import logging
from typing import List,Dict, Optional

#configurar logging
logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s- %(levelname)s- %(message)s")
    
#cargar las variables del entorno
def load_env()->Optional[Dict[str,str]]:
    load_dotenv()
    api_key=os.getenv("API_KEY")
    search_engine_id=os.getenv("SEARCH_ENGINE_ID")

    if not api_key or not search_engine_id:
     logging.error("api key o search engine id no estan cargados")
     return None
    return {
    'api_key': api_key,
    'search_engine_id': search_engine_id
}

def main():
    env_vars=load_env()
    logging.info("variables cargadas")

if __name__ =="__main__":
    main()