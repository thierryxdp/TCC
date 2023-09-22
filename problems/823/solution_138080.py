def faltante(L):
    '''função que retorna a peca faltante de um quebra cabeça dados uma lista n-1
lis->int'''
    proximo = 0
    while proximo<= len(L):
        if proximo in not L:
    proximo = proximo + 1
    return proximo