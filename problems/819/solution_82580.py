def filtraMultiplos(lista_numero,n):
    """Dada a lista de entrada, retorne os números divisíveis por n"""
    numeros = []
    i = 0
    while i<len(lista_numero):
        if lista_numero[i]%n==0:
            numeros = numeros+(list.extend(lista_numero,i)
        i = i+1
    return numeros