def filtra_pares(numeros):
    '''função que dados os numeros retorna apenas os pares
    int->int'''
    saida = ()
    if numeros[0]%2 == 0:
        saida = saida + (numeros[0],)
    if numeros[1]%2 == 0:
        saida = saida + (numeros[1],)
    if numeros[2]%2 == 0:
        saida = saida + (numeros[2],)
    if numeros[3]%2 == 0:
        saida = saida + (numeros[3],)
        return saida