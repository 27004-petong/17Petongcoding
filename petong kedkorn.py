print("โปรแกรมตรวจจับความเร็ว")

carspeed = int(input("กรอกความเร็วของรถ"))


if carspeed <=80:
    print("ปลอดภัย")
elif carspeed <=100:
    print("เตือน")
elif carspeed<=120:
    print("เสี่ยงถูกปรับ")

else:
    print("ผิดกฎหมาย")


print("จัดทำโดย นาย ปัณณวัฒน์ เกษกร ชั้น ม.4/4 เลขที่ 17")