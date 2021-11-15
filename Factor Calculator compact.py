n = int(input("Fill in a number you would like to check the factors of: "))
for i in range(2,n): 
    if (n % i) == 0: print("A factor of",n,"is",i)
input("press enter to exit")