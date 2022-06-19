

print("Enter the value of A: ")
A = int(input())
print("Enter the operator value: ")
Opr = input()
print("enter the value B: ")
B = int(input())
if A== 45 and B==3 and Opr=="*":
    print("555")
elif A== 56 and B==9 and Opr=="+":
    print("77")
elif A== 56 and B==6 and Opr=="/":
    print("4")
elif Opr =="+":
    print("The addithon of the value is: ",A+B)
elif Opr=="*":
    print("The the multipl of the value is: ", A * B)
elif Opr == "-":
    print("The the Substraction of the value is: ", A - B)
elif Opr == "/":
    print("The the Division of the value is: ", A / B)
else:
    print("Please enter correct Operator: ")
