"""
В задании создан словарь, с информацией о разных устройствах.

Необходимо запросить у пользователя ввод имени устройства (r1, r2 или sw1).
 И вывести информацию о соответствующем устройстве на стандартный поток вывода (информация будет в виде словаря).
"""
london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}

device = input('Введите имя устройства: ')
args_dev = tuple(london_co[device].keys())
param = input(f'Введите имя параметра {args_dev}: ')
try:
    print(london_co[device][param.lower()])
except KeyError:
    print('Такого параметра нет')
