def soma_h(n):
    '''retorna a soma de n ternos do somatorio
    1+1/2+1/3+...+1/n;int -> float'''
    soma=0
    for numero in range(1,n):
        soma=soma+(1/numero)
    return soma