lower = 1
upper = 250

print("Prime numbers between", lower, "and", upper, "are:")

file = open("results.txt","w")

for num in range(1, 251):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           file.write(str(num) + "\n")
           
file.close()