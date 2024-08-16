# Ex10 - Number
# Enter 5 numbers and find maximum and minimum value
# Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0
number=""
for i in range(5):
    n=input()
    number+=str(n)
    max=number[0]
    min=number[0]
    for i in range(len(number)):
        if number[i]>max:
            max=number[i]
        elif number[i]<min:
            min=number[i]
print("Max=",max)
print("Min=",min)



