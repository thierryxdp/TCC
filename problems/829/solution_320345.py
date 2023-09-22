def soma_h(n):
      """Recebe um número inteiro e retorna a soma_h/int->float"""
      if type(n)!=int:
            print("O número deve ser inteiro")
      else:
            soma=0
            for i in range(1,n+1):
                  soma+=1/i
            return round(soma,2)