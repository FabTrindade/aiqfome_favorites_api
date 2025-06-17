import requests

FAKESTORE_URL = "https://fakestoreapi.com/products/"

def get_product_by_id(product_id: int):
    try:
        response = requests.get(f"{FAKESTORE_URL}{product_id}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        # TODO: Melhorar tratamento de falha de integração externa
        print(f"Erro ao buscar produto {product_id}: {e}")
        return None
