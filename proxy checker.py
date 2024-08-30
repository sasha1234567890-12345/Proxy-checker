import requests

def check_proxy(proxy):
    try:
        response = requests.get("http://www.google.com", proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            print(f"Прокси {proxy} работает!")
        else:
            print(f"Прокси {proxy} не работает. Статус: {response.status_code}")
    except Exception as e:
        print(f"Ошибка с прокси {proxy}: {e}")

# Пример использования
proxy = "http://proxy:port"  # Замените на ваш прокси
check_proxy(proxy)
