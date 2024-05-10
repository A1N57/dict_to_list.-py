while True:
    try:
        num1 = float(input("Enter first num: "))
        num2 = float(input("Enter second num: "))
    except ValueError as e:
        print(e)
        print("You must enter numbers!")
        continue
    
    print(num1 / num2)
    answer = input("Do you want continue yes or no? ")
    if answer == 'no':
        break

   