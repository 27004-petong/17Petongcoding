point1 = int(input("คะแนนวิชา1:  "))
point2 = int(input("คะแนนวิชา2:  "))
point3 = int(input("คะแนนวิชา3:  "))


total_point = point1 + point2 + point3
average = total_point /3


if average < 60:
    print("คะแนนรวมของคุณ = ", total_point)
    print("คะแนนเฉลี่ย 3 วิชา = ", average)
    print("ควรปรับปรุง")
elif average <80:
    print("ผ่าน")
else:
    print("ดีเยี่ยม")