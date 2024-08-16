# Ex7 - number
# Enter number in range 10 - 20 until you enter other number out of range
# display "Continue" if number in range 10 - 20
# display "Out of range" if number difference from range 10 - 20
outRange=False
while not outRange:
    n=int(input("Enter number: "))
    if n>10 and n<20:
        print("Contiue")
    else:
        print("Out reange")
        outRange=True