# Ex8 - String
# We have text = "9394884039"
# Q1 - How many number 8 in string
# text = "9394884039"
# count=0
# for i in range(len(text)):
#     if int(text[i])==8:
#         count+=1
# print(count)
# Q2 - What is first index of letter 8
text = "9394884039"
isFound=False
for i in range(len(text)):
    if int(text[i])==8 and not isFound:
        isFound=True
        print(i)
        

