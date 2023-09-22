def filtraMultiplos(numeros:tuple,x):
    """Função que filtra os multiplos de um número n , lista-->lista"""
    lista=[] 
    n=0
    while n < len(numeros):
        if numeros[n] % x == 0 :
            list.append(lista,numeros[n])
        n=n+1
    return lista