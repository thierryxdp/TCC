def soma_h(n):
    '''funcao recebe um valor n e realiza o somatoria
    de h, onde h e o fatorial de n'''
    soma=1
    for n in range(2,n+1):
        soma= soma+1
    return round(soma,2)