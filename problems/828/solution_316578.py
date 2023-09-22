def primo(n):
    '''função que dado um numero inteiro positivo, verifica
    se o mesmo é primo ou não'''
    resposta = 0
    num = 1
    for x in range(n):
        if n%num==0:
            resposta = resposta + 1
        num = num + 1
        
    return resposta > 2