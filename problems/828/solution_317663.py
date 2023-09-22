def qtd_divisores(n):
    '''
    Função que recebe um numero e conta quantos divisores esse
    numero tem
    int--->int
    '''
    if n<0:
        return 0
    d=n
    resposta=0
    while d!=0:
        if n%d==0:
            resposta+=1
        d=d-1
    return resposta

def primo(n):
    '''
    Função que dado um numero, diz se ele é um numero primo ou não
    int--> boolean
    '''
    teste=qtd_divisores(n)
    if teste=2:
        return True
    else:
        return False