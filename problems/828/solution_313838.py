def primo(n):
    '''Função que recebe um número inteiro e verifica se esse
    número é primo ou não.
    entrada da função: int
    saída da função: bool'''
    
    multipl=0
    
    for count in range(2,n):
        if (n % count == 0):
            multipl += 1

        if(multipl == 0):
            x = True
  
        else:
            x = False
            
      
    return x