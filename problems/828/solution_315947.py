def primo(n):
    '''Funcao que recebe um nuemro inteiro positivo e 
    verifica se ele eh primo ou nao, caso seja retorna 
    True, caso não, retorna False.
    int -> bool'''
    divisores = []
    for divisor in range(1,n+1):  
        if n % divisor == 0: 
            divisores = divisores + [divisor]
    if divisores == [1,n]:
        return True
    else:
        return False
#TESTE
# primo(7) == True
# primo(13) == True
# primo(25) == False