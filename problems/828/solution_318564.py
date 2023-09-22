def primo(X):
  '''Função que, dado um número inteiro X positivo, verifica se o número é primo ou não
  int -> bool'''

  resultado = []

  if X > 0:
    for i in range(2,X):
      if not X % i == 0:
        '''Não existe nenhum número no intervalo [2,X) que seja divisor de X'''
        list.append(resultado,True)
      else:
        list.append(resultado,False)
    
    if False not in resultado:
      return True
    else:
      return False