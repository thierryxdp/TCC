def faltante(L):
    '''Recebe uma lista N de entrada e retorna qual número inteiro falta nessa sequência numérica; list->int'''
    numero=1
    while numero<=len(L)+1:
        if numero in L:
            numero=numero+1
        else:
            return numero