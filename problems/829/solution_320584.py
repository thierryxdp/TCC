def soma_h(n):
    '''Retorna a soma do inverso dos número até N.
    int -> int'''
    soma=0
    for i in range(n+1):
        soma = soma + 1/i
    return soma