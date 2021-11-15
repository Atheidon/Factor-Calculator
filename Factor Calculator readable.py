#A SIMPLE FACTOR CALCULATOR

#asking for a number
number = int(input("Fill in a number you would like to check the factors of: "))
#creating a range, from 2 to the number itself
for i in range(2,number): 
        #if n divided by i (a number in range 2 to n) has no leftovers, print i
        if (number % i) == 0: 
            #print the individual factors
            print("A factor of",number,"is",i)
input("press enter to exit")

#note: if it doesn't display any factors, it's either a prime number or a negative number (in which case you should fill in the positive version and make the factors negative)