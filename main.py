import requests

from dotenv import load_dotenv

import os


def load_variable():
    try:
        load_dotenv()
        api_key = os.getenv("API_KEY")
        search_engine_id = os.getenv("ENGINE_ID")

        if not api_key:
            return ValueError("No se encontro el api key")
        if not search_engine_id:
            return ValueError("No se encontro el search engine id")

        print(f"Tus variables de entorno son el api key: {api_key} y search engine id: {search_engine_id}")

        return api_key, search_engine_id

    except ValueError as e:
        print(e)
        return None

def requestAPI(api_key, search_engine_id):
    try:
        query =  'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'
        page = 1
        lang = "lang_es"

        url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}&start={page}&lr={lang}"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"data: {data}")
        else:
            return ValueError("Algo salio mal con la solicitud")
    except ValueError as e:
        print(e)
        return None

def main():
    api_key, search_engine_id = load_variable()
    requestAPI(api_key, search_engine_id)

if __name__ == "__main__":
    main()