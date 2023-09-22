def filtra_pares(a,b,c,d):
    '''Função que recebe uma tupla e retorna a mesma tupla
    com somente elementos pares; tupla->tupla'''
    nova = ()
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        filtragem = nova+a,b,c,d
        return filtragem