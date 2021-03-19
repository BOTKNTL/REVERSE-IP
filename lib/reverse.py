import requests
from multiprocessing import Pool
import argparse
from colorama import Fore
class ReverseIP(object):

    def __init__(self, thread, ip, proxy):
        self.thread = thread
        self.ip = ip
        self.proxy = proxy

    def reverse(self, ip, proxy):
        try:
            http_proxy = 'http://'+proxy
            https_proxy = 'https://'+proxy
            proxyDict = {
                'http': http_proxy,
                'https': https_proxy
            }
            api = 'http://api.hackertarget.com/reverseiplookup/?q='+ip
            request = requests.get(api, proxies=proxyDict, timeout=10)
            if request:
                if 'error' in request.text or 'No DNS' in request.text:
                    pass
                elif 'API count exceeded' in request.text or 'Bad Request' in request.text:
                    pass
                elif '<' in request.text or '>' in request.text:
                    pass
                else:
                    print(Fore.GREEN ,'Reversing IP: {}\n'.format(ip))
                    print(Fore.LIGHTMAGENTA_EX ,'=> {}'.format(request.text))
                    open('reversed.txt','a').write(request.text+'\n')
                    pass
        except Exception as e:
            print(Fore.RED, 'Error IP: {}'.format(ip))
            open('err_ip.txt','a').write(ip+'\n')

    def run(self):
        with Pool(self.thread) as worker:
            worker.starmap(self.reverse, zip(self.ip, self.proxy))
            worker.close()
            worker.join()