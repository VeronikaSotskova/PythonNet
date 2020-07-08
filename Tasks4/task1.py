def get_vlans_from_conf(comm):
    startInd_comm1 = comm.find('vlan') + 5
    return comm[startInd_comm1:].split(',')


"""
4.1
Обработать строку nat таким образом, чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.
"""

NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
NAT = NAT.replace('Fast', 'Gigabit')
print(NAT)

"""
4.2
Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX
"""

mac = 'AAAA:BBBB:CCCC'
macs = mac.replace(':', '.')
print(macs)

"""
4.3
Получить из строки config список VLANов вида: ['1', '3', '10', '20', '30', '100']
"""

config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
vlans_conf = config.split()[4].split(',')
print(vlans_conf)

"""
4.4
Список vlans это список VLANов, собранных со всех устройств сети, поэтому в списке есть повторяющиеся номера VLAN.
Из списка нужно получить уникальный список VLANов, отсортированный по возрастанию номеров.
"""

vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
vlans = set(vlans)
print(vlans)

"""
4.5
Из строк command1 и command2 получить список VLANов, которые есть и в команде command1 и в команде command2.
Результатом должен быть список: ['1', '3', '8']
"""

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

vlans_comm1 = get_vlans_from_conf(command1)
vlans_comm2 = get_vlans_from_conf(command2)
res = list(set(vlans_comm1).intersection(set(vlans_comm2)))
print(res)

"""
4.6
Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:

Protocol:               OSPF
Prefix:                 10.0.24.0/24
AD/Metric:              110/41
Next-Hop:               10.0.13.3
Last update:            3d18h
Outbound Interface:     FastEthernet0/0
"""

ospf_route = 'OSPF        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_sett = ospf_route.split()
ospf_names = [['Protocol:', ospf_sett[0]],
              ['Prefix:', ospf_sett[1]],
              ['AD/Metric:', ospf_sett[2].strip('[]')],
              ['Next-Hop:', ospf_sett[4]],
              ['Last update:', ospf_sett[5]],
              ['Outbound Interface:', ospf_sett[6]]]
width = 20
for x in ospf_names:
    name, ans = x
    print(f'{name:{width}} {ans:{width}}')

"""
4.7
Преобразовать MAC-адрес mac в двоичную строку такого вида: 101010101010101010111011101110111100110011001100
"""

mac = 'AAAA:BBBB:CCCC'
macs_2 = mac.split(':')
res = ''
for m in macs_2:
    res += bin(int(m, 16))[2:]
print(res)

"""
4.8
Пример вывода для адреса 10.1.1.1:
ширина столбца 10 символов
10        1         1         1
00001010  00000001  00000001  00000001
"""

ip = '192.168.3.1'
width = 8
oct1, oct2, oct3, oct4 = ip.split('.')
print(type)
print(f'''
     IP address:
     {oct1:{width}} {oct2:{width}} {oct3:{width}} {oct4:{width}}
     {int(oct1):>0{width}b} {int(oct2):>0{width}b} {int(oct3):>0{width}b} {int(oct4):>0{width}b}''')