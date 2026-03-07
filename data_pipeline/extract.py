import requests
import time

BASE_URL = "https://swapi.dev/api"


def fetch_data(endpoint):
    url = f"{BASE_URL}/{endpoint}/"
    all_results = []

    session = requests.Session()

    print(f"Iniciando extração de: {endpoint}")

    while url:
        try:
            response = session.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()

            all_results.extend(data["results"])
            url = data.get("next")

            if url:
                print(f"Dados parciais coletados: {len(all_results)}. Indo para próxima página...")
                time.sleep(0.2)

        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar {url}: {e}")
            break

    print(f"Extração finalizada! Total de registros: {len(all_results)}")

    return all_results