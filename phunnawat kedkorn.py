import random
answer = random.randint(1,100)
count = 0
 
while True:
    guess = int(input("ทายเลข 1-100:"))
    count += 1

    if guess > answer:
        print("มากไป")
    elif guess > answer:
        print("น้อยไป")
    else:
        print("ถูกต้อง")
        print("คุณทาย", count, "ครั้ง")
        break

