import random
random_num = random.randint(1, 5)
while True:
    num = int(input("Enter from 1 to 5: "))
    if num != random_num:
        print(random_num)
        print("Try again...")
        continue
    print("Congratulation", random_num)
    
    break