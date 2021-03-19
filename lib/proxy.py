import proxygrab
from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException
import urllib.request
import socket
import urllib.error
from colorama import Fore
from multiprocessing.dummy import Pool
import time

class Checker(object):

    PROXY = []

    def __init__(self, thread_count, proxy):
        self.thread_count = thread_count
        self.proxy = proxy


    def is_bad_proxy(self, pip):
        try:
            proxy_handler = urllib.request.ProxyHandler({'http': pip})
            opener = urllib.request.build_opener(proxy_handler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)
            req=urllib.request.Request('http://www.google.com')
            sock=urllib.request.urlopen(req)
        except urllib.error.HTTPError as e:
            return e.code
        except Exception as detail:
            return True
        return False

    def check(self, proxyList):
        
        socket.setdefaulttimeout(120)
        if self.is_bad_proxy(proxyList):
            pass
        else:
            self.PROXY.append(proxyList)

    def run(self):
        with Pool(self.thread_count) as worker:
            worker.map(self.check, self.proxy)
            worker.close()
            worker.join()

        with open('vuln-proxy.txt', 'w') as f:
            for i in self.PROXY:
                f.write(i + '\n')

def create_proxy():

    PROXY = []

    print('Scrape Proxy')
    try:
        print('Scrape From Proxy_List_Scrapper')
        SSL = 'https://www.sslproxies.org/',
        GOOGLE = 'https://www.google-proxy.net/',
        ANANY = 'https://free-proxy-list.net/anonymous-proxy.html',
        UK = 'https://free-proxy-list.net/uk-proxy.html',
        US = 'https://www.us-proxy.org/',
        NEW = 'https://free-proxy-list.net/',
        SPYS_ME = 'http://spys.me/proxy.txt',
        PROXYSCRAPE = 'https://api.proxyscrape.com/?request=getproxies&proxytype=all&country=all&ssl=all&anonymity=all',
        PROXYNOVA = 'https://www.proxynova.com/proxy-server-list/'
        PROXYLIST_DOWNLOAD_HTTP = 'https://www.proxy-list.download/HTTP'
        PROXYLIST_DOWNLOAD_HTTPS = 'https://www.proxy-list.download/HTTPS'
        PROXYLIST_DOWNLOAD_SOCKS4 = 'https://www.proxy-list.download/SOCKS4'
        PROXYLIST_DOWNLOAD_SOCKS5 = 'https://www.proxy-list.download/SOCKS5'
        ALL = 'ALL'
        scrapper = Scrapper(category=ALL, print_err_trace=False)
        data = scrapper.getProxies()

        for item in data.proxies:
            PROXY.append('{}:{}\n'.format(item.ip, item.port))
    except:
        pass
    try:
        proxy_types = ('http', 'https', 'socks4', 'socks5')
        for i in proxy_types:
            PROXY.append(proxygrab.get_proxy(i))
    except:
        pass
    print('Check Proxy')

    # Terserah mw pake thread brp tinggal ganti doang
    runner = Checker(100, PROXY)
    runner.run()

    return print('Done Scrape Proxy')