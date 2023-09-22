def primo(n):
      """Recebe um número inteiro e positivo e retorna se ele é primo ou não/int->bool"""
      if type(n)!=int and n<0:
            print("O número deve ser inteiro e positivo")
      else:
            if n==0 or n==1:
                  return False
            else:
                  lista=list()
                  for i in range(1,n+1):
                        if n%i==0:
                              lista.append(i)
                  if len(lista)==2 and lista[0]==1 and lista[1]==n:
                        return True
                  else:
                        return False