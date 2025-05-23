a=int(input("Enter the first term of the series: "))
d=int(input("Enter the common difference of the series: "))
n=int(input("Enter the number of terms you want to print: "))
for i in range(a,(a+(n-1)*d)+1,d):
    print(i)
