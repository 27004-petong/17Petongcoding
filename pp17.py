print("โปรแกรมคำนวณค่า bmi")

weight = float(input("น้ำหนัก (kg): "))
height = float(input("ส่วนสูง (cm): "))

bmi = weight / (height ** 2)

print(f"BMI ของคุณคือ {bmi:.2f}")

if bmi < 18.5:
    print("ผอม")
elif bmi < 23:
    print("ปกติ")
elif bmi < 25:
    print("น้ำหนักเกิน")
else:
    print("อ้วน")

print("จัดทำโดย นายปํณณวัฒน์ เกษกร เลขที่17 ม.4/4")