def qtd_divisores(n):
      """Recebe um número inteiro e retorna a quantidade de divisores do número/int->int"""
      if type(n)!=int:
            print("o número deve ser inteiro")
      else:
            j=0
            i=1
            while i<=n:
                  if n%i==0:
                        j+=1
                  i+=1
            if n<0:
                  return 0
            else:
                  return j