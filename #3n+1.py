#3n+1
import time

t= True
a = True



print('''   Hello there, this is a programme that you use to test some numbers in Collatz conjecture. 
      
        Incase you weren't familiar with it here is what it does:
      
            • First, you type a positive number.
            • If the number is even, you divide it by 2.
            • If the number is odd, you multiply by 3 and add 1.
            • The conjecture states that there is no number that wont end up in 1 if you applied this operations to it.
      
            You think you can find a number that can't satisfy this conjecture?. Goodluck!
      
                If you want to exit type 0.
      

      
      ''')

while t:
    n = int(input('Type a number :     '))
    if n ==0:
        print(' \n \n         Quit. \n \n')
        break
    print(n)
    while a:
        if n % 2 == 0:
                n //= 2
                print(n)
                time.sleep(0.1)
        else:
                n = 3*n + 1
                print(n)
                time.sleep(0.1)
        if n ==1:
            break
    
          















