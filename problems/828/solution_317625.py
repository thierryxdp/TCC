def primo(num):
    '''
       Dado um número a função verifica esse número é primo 
       ou não e retorna True quando o número é primo e False
       quando o número não é primo.
       int -> bool
    '''
    for i in range(2,num-1):
        if num%i == 0:
            saida = False
        else:
            saida = True
    return saida