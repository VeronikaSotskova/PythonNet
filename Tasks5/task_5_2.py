"""
Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24
Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
"""
ip_inp = input('Введите ip в формате X.X.X.X/mask: ')
ip, mask = ip_inp.split('/')
width = 8
ip_oct1, ip_oct2, ip_oct3, ip_oct4 = ip.split('.')
bin_mask = '1' * int(mask) + '0' * (32 - int(mask))
mask_oct1, mask_oct2, mask_oct3, mask_oct4 = bin_mask[::8]
print(f'''
     Network:
     {ip_oct1:{width}} {ip_oct2:{width}} {ip_oct3:{width}} {ip_oct4:{width}}
     {int(ip_oct1):>0{width}b} {int(ip_oct2):>0{width}b} {int(ip_oct3):>0{width}b} {int(ip_oct4):>0{width}b}

     Mask:
     {int(bin_mask[0:8], 2):<{width}} {int(bin_mask[8:16], 2):<{width}} {int(bin_mask[16:24], 2):<{width}} {int(bin_mask[24:32], 2):<{width}}
     {bin_mask[0:8]:>0{width}} {bin_mask[8:16]:>0{width}} {bin_mask[16:24]:>0{width}} {bin_mask[24:32]:>0{width}}
     ''')


def check_if_host(ip, mask):
    oct1, oct2, oct3, oct4 = ip.split('.')
    return


def mask_bit_to_dec(mask):
    whole_part_mask = mask / 8
    remains = mask % 8
    if whole_part_mask == 0:
        return int(remains*'1', 2), 0, 0, 0
    else:

        return
