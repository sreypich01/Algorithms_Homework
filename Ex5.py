# Ex5 - String 
# We have text = "454639"
# Q1 - Count odd and even number in text
text = "454639"
odd_number=0
even_number=0
for i in range(len(text)):
    if int(text[i])%2==1:
        odd_number+=1
    else:
        even_number+=1
print("odd number: ", odd_number)
print("even number: ",even_number)
# Q2 - Sum all number 
text = "454639"
sum=0
for i in range(len(text)):
        sum += int(text[i])
print(sum)
# Q3 - Sum only even number 
text = "454639"
sum=0
for i in range(len(text)):
    if int(text[i])%2==0:
        sum += int(text[i])
print(sum)
# Q4 - Reverse
text = "454639"
reverse=len(text)-1
result=""
for i in range(len(text)):
    result+=text[reverse-i]
print(result)