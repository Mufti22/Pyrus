import requests
import urllib3
import json
# Отключаем предупреждения об ошибках безопасности SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_BASE_URL = "https://pyrus.com/api/v4/"
API_LOGIN = "XXXXXXX"
API_KEY = "XXXXXXX"

def prerequest():
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({"login": API_LOGIN, "security_key": API_KEY})
    try:
        response = requests.post(API_BASE_URL + "auth", headers=headers, data=data, verify=False)
        if response.status_code == 200:
            print("Success")
            return response.json()['access_token']
        else:
            print(f"Authentication failed with status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def download_catalog(catalog_id, token):
    download_url = f"{API_BASE_URL}catalogs/{catalog_id}"
    headers = {'Authorization': f'Bearer {token}'}

    try:
        response = requests.get(download_url, headers=headers, verify=False)
        if response.status_code == 200:
            filename = f"catalog_{catalog_id}.json"
            with open(filename, 'wb') as file:
                file.write(response.content)

            print(f"Catalog downloaded successfully as {filename}.")
        else:
            print(f"Failed to download catalog. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error during catalog download: {e}")

    return None

# Получаем токен
token = prerequest()

# Если токен получен успешно, скачиваем каталог
if token:
    catalog_id_to_download = 2608  # Замените на нужный ID каталога
    download_catalog(catalog_id_to_download, token)
