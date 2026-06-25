print("โปรแกรมคำนวณ ค่าBMIและแปลผลสุขภาพ")
W1 = int(input("น้ำหนัก(kg)"))
H1 = int(input("ความสูง(cm)"))

total = W1 / H1 * H1

average = total 

if average <=18.5:
    print("น้ำหนักน้อย")

elif  average  >=18.6-22.9:
    print("ปกติ")

elif  average  >=23-24.9:
    print("น้ำหนักเกิน")

elif  average  <=25:
    print("อ้วน")