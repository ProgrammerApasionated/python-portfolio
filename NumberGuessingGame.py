print ("This program will guess a number with a range of numbers \n")
num1= int(input("Enter the first number,lower than the second: \n"))
num2= int(input("Enter the second number, higher than the first one: "))
while num1 == num2 or num1 > num2:
    print ("The numbers can't be even or the first one higher than the second")
    num1= int(input("Enter the first number,lower than the second\n"))
    num2= int(input("Enter the second number, higher than the first one\n"))
num_guess=num2//2
respuesta=input (f"Is your number {num_guess} T or F,")
if respuesta== "T":
    print (f"Your number is {num_guess}")
else:
    respuesta= input ("Is your number higher or lower, H or L : ")
    if respuesta == "H":
        for i in range (num_guess,num2 + 1):
            confirmation= input (f"Is your number {i} Y or N : ")
            if confirmation == "Y":
                print (f"Your number is {i}")
                break
            else:
                print (f"{i} is not your number")
                
    else:
        for i2 in range (num1, num_guess + 1):
            confirmation= input (f"Is your number {i2} Y or N : ")
            if confirmation == "Y":
                print (f"Your number is {i2}")
                break
            else:
                print (f"{i2} is not your number")


