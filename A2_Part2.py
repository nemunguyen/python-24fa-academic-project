print("Lets create the First data sample with 6 Integers, 1 <= Value <= 9")
data1=[]
number1=1
while number1<=6:
    n1=int(input("Please enter [First Sample - Item number %d] -> " %(number1)))
    data1.append(n1)
    number1=number1+1
print("")
print("Lets create the Second data sample with 6 Integers, 1 <= Value <= 9")
data2=[]
number2=1
while number2<=6:
    n2=int(input("Please enter [Second Sample - Item number %d] -> " %(number2)))
    data2.append(n2)
    number2=number2+1
print("")
print("Original items of the Data Sample 1")
print(data1[0], ", ", data1[1], ", ", data1[2], ", ", data1[3], ", ", data1[4], ", ", data1[5])
print("")
print("Original items of the Data Sample 2")
print(data2[0], ", ", data2[1], ", ", data2[2], ", ", data2[3], ", ", data2[4], ", ", data2[5])
print("")
print("Sorted items of the Data Sample 1")
print(sorted(data1))
print("")
print("Sorted items of the Data Sample 2")
print(sorted(data2))
data1.extend(data2)
print("")
print("Items of the Data Sample 1 and Sample 2")
print(data1)
print("")
print("Sorted items of the Data Sample 1 and Sample 2")
data1.sort()
print(data1)
print("")
nodup=set(data1)
print("Unique items of the Data Sample 1 and Sample 2")
print(nodup)


