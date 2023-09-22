def faltante(L):
    '''função que retorna a peca faltante de um quebra cabeça dados uma lista n-1
lis->int'''
    proximo = 0
    faltante = 0
    while proximo < len(L):
        if proximo in L:
            faltante = max(L)+1            
    proximo = proximo + 1
    return faltante