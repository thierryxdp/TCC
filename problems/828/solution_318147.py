def primo(numero):
    '''Essa função verifica se um número inteiro positivo é primo ou não,
    int->bool'''
    soma=0
    for x in range(1,(numero+1)):
       if numero%x==0:
         soma+=1
    if soma==2:
      return True
    else:
      return False