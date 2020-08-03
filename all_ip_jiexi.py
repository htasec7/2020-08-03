import requests
from time import sleep

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
}
proxy = {
    "http":"183.149.97.204:45326"
}
def get_ip(start='1.1.1.1'):
    file = open('ip_succ.txt', 'w')
    a = int(start.split('.')[0])
    b = int(start.split('.')[1])
    c = int(start.split('.')[2])
    d = int(start.split('.')[3])
    for b in range(1,255):
        for c in range(2,255):
            for d in range(1,255):
                url = "http://{}.{}.{}.{}".format(a,b,c,d)
                try:
                    res = requests.get(url,headers=headers,timeout=6)
                    sleep(3)
                    if res.status_code == 200:
                        file.write(url + '\n')
                    else:
                        print("该IP不能直接访问:",url)
                except:
                    print("本地IP请求超时！",url)

get_ip()