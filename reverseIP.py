import requests
from lib.reverse import ReverseIP
from lib.proxygrabber import create_proxy
def banner():
    banner = '''
        |  __ \|  ____\ \    / /  ____|  __ \ / ____|  ____|  |_   _|  __ \ 
        | |__) | |__   \ \  / /| |__  | |__) | (___ | |__ ______| | | |__) |
        |  _  /|  __|   \ \/ / |  __| |  _  / \___ \|  __|______| | |  ___/ 
        | | \ \| |____   \  /  | |____| | \ \ ____) | |____    _| |_| |     
        |_|  \_\______|   \/   |______|_|  \_\_____/|______|  |_____|_|     
                                                                     
    Github      : https://github.com/ranggaggngntt/
    Facebook    : https://facebook.com/Rangga.Haxor/
    '''

    return print(banner)

if __name__ == '__main__':
    banner()
    ip_file = input('IP List: ')
    thread = int(input('Thread: '))

    with open(ip_file, 'r') as f:
        ip = f.read().splitlines()

    temp_list_ip = [ip[i:i+20] for i in range(0, len(ip), 20)]
    
    while len(temp_list_ip) > 0:
        try:
            p = open('proxy.txt', 'a')
            p.truncate(0)
            p.close()

            create_proxy()

            with open('proxy.txt', 'r') as f:
                proxies = f.read().splitlines()

            for i in range(len(proxies)):
                try:
                    ReverseIP(thread, temp_list_ip[i], proxies[i])
                    temp_list_ip.remove(temp_list_ip[i])
                except Exception:
                    break
        except Exception as e:
            print(e)
            exit()