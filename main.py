import requests


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        print(response)
    except requests.exceptions.ConnectionError:
        print('Нет соединения с интернетом')

def main():
    ip = input('Enter your ip-adress: ')

    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()
