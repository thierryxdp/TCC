def filtraMultiplos(lista_numero,n):
    """Dada a lista de entrada, retorne os números divisíveis por n"""
    i=0
    numeros = ''
    while i<len(lista_numero):
        if lista_numero[i]%n==0:
            numeros = list.append(numeros,lista_numero[i])
        i = i + 1
    return numeros