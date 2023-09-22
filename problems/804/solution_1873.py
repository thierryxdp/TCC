filtra_pares(numeros):
    '''retorna uma nova tupla contendo apenas os elementos pares da tupla original'''
    pares=()
    for n in numeros:
        if n%2==0:
            pares.append(n)
    return pares