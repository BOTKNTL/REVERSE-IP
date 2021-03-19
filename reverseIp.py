import time
from lib.proxy import create_proxy
import requests
from multiprocessing import Pool
from lib.reverse import ReverseIP

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

def main():
    temp_used = []
    temp = []
    proxies = []
    file = input('Nama File: ')
    thread = int(input('Thread: '))
    with open(file, 'r') as f:
        ip = f.read().split()
    while len(ip) > 0:
        proxy = open('vuln-proxy.txt','a')
        proxy.truncate(0)
        proxy.close()

        if len(temp_used) == 0:
            pass
        else:
            for used in temp:
                try:
                    temp_used.remove(used)
                except:
                    continue

        create_proxy()
        with open('vuln-proxy.txt','r') as f:
            p = f.read().split('\n')

        for pr in p:
            proxies.append(pr)
        proxies = list(set(proxies))
        try:

            for s in range(len(proxies)):
                try:
                    temp_used.append(ip[s])
                except:
                    continue

            temp_ip = open('temp-ip.txt','a')
            temp_ip.truncate(0)

            for ti in temp_used:
                temp_ip.write(ti+'\n')
            temp_ip.close()

            for t in range(len(proxies)):
                try:
                    temp.append(ip[t])
                except:
                    continue

            for k in temp:
                try:
                    ip.remove(k)
                except:
                    continue

        except Exception as e:
            print(e)
            continue
        
        ReverseIP(thread, temp_used, proxies).run()
        continue
if __name__ == '__main__':
    banner()
    main()