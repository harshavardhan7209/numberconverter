import math
def deccon(quest, chooser):
    x = quest
    y = []
    while x!=0:
        y.append(str(x%chooser))
        x = int(x/chooser)
    z = ''
    for i in range(len(y)):
        z = z+y[i]
    return z[::-1]
def baccon(quest, chooser):
    sum = 0
    cc = len(str(quest))
    dd = 0
    while (cc)!=0:
        x = int(int(str(quest)[dd]) * math.pow(chooser,cc-1))
        sum+=x
        dd = dd+1
        cc = cc-1
    return sum
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
y = int(input("What do you want todo:\n1. Decimal to Binary\n2. Decimal to Octal\n3. Binary to Decimal\n4. Octal to Decimal\n5. Octal to Binary\n6. Binary to Octal \n: "))
x = int(input("Enter a number for conversion: "))
b = False
d = False
o = False
sdig = len(str(x))
sum=0
for i in range(len(str(x))):
    sum = sum+float(str(x)[i])
ob = 0
def dtb(x):
    print("Binary Digit is: ("+str(deccon(x, 2))+")"+str(2).translate(SUB))
def dto(x):
    print("Octal Digit is: ("+str(deccon(x, 8))+")"+str(8).translate(SUB))
def btd(x):
    print("Decimal Digit is: ("+str(baccon(x, 2))+")"+str(10).translate(SUB))
def otd(x):
    print("Decimal Digit is: ("+str(baccon(x, 8))+")"+str(10).translate(SUB))
def otb(x):
    print("Binary Digit is: ("+str(deccon(baccon(x, 8), 2))+")"+str(2).translate(SUB))
def bto(x):
    print("Octal Digit is: ("+str(deccon(baccon(x, 2), 8))+")"+str(8).translate(SUB))
if y==1 and sum/sdig<=1:
    ob = 10
    o = True
    dtb(x)
elif y==2 and sum/sdig<=7:
    ob = 10
    b = True
    dto(x)
elif y==3 and sum/sdig<=1:
    ob = 2
    o = True
    btd(x)
elif y==4 and sum/sdig<=7:
    ob = 8
    b = True
    otd(x)
elif y==5 and sum/sdig<=1:
    ob = 8
    d = True
    otb(x)
elif y==6 and sum/sdig<=7:
    ob = 2
    d = True
    bto(x)
else:
    print("Invalid selection or number.")
    exit()
xyz = input("Do you want to continue and get other conversion values: ")
if xyz == "y":
    if b==True:
        if ob==8:
            btd(x)
        elif ob==10:
            bto(x)
    elif d==True:
        if ob==2:
            dto(x)
        elif ob==8:
            dtb(x)
    elif o==True:
        if ob==2:
            otd(x)
        elif ob==10:
            otb(x)
