def fatorial(n):
      if type(n)!=int  and n<0:
            print("O número precisa ser positivo")
      elif n==0 or n==1:
            return 1
      else:
            return n*fatorial(n-1)