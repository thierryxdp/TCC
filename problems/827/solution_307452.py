def divisores (n):
     cont = 0
     for divisor in range (1, n+1):
          if (n % divisor == 0):
               cont += 1
     return cont