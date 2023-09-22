def qtd_divisores(n):
      """Recebe um número inteiro e retorna a quantidade de divisores do número/int->int"""
      if type(n)!=int:
            print("o número deve ser inteiro")
      else:
            j=0
            i=1
            if n<0:
                  x=-n 
                  while i<=x:
                        if x%i==0:
                              j+=1
                        i+=1
            else:
                 while i<=n:
                        if n%i==0:
                              j+=1
                        i+=1 
            if n<0:
                  j=j*2
                  return j
            else:
                  return j