#โจรย์ข้อ1

#อายุ
def calculate_mhr (age):
    return 220 - age

#อัตราการเต้น
def calculate_mhr_zone2(mhr):
    low = 0.6 * mhr
    up = 0.7 * mhr
    return low,up

age = int(input("อายุปัจุบัน: "))
mhr = calculate_mhr (age)
low_zone2, up_zone2 = calculate_mhr_zone2(mhr)

#ผลลัพธ์
print (f'อัตราการเต้นของหัวใจตํ่าที่เหมาะสม : {up_zone2:.2f}')
print (f'อัตราการเต้นของหัวใจตํ่าที่เหมาะสม : {low_zone2:.2f}')
