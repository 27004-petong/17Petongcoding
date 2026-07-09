print("โปรแกรมแมาสูตรคูณ")

stat = int(input("แม่เริ่มต้น"))
end =  int(input("แม่สุดท้าย"))

for i in range(stat , end +1):
    print("สูตรคูณแม่")
    for loop in range (1,13):
        print(i,"x", loop , "=" ,i*loop)


print("จัดทำโดย นาย ปํณณวัฒน์ เกษกร ม.4/4 เลขที่17")