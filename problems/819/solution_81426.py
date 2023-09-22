def filtraMultiplos(lista,n):
    """Função que filtra os múltiplos de um número
    list, int --> list"""
     i = 0
    resultado = []
    while i<len(lista):
        if lista[i]%divisor == 0:
            resultado = resultado + [lista[i]]
        i=i+1

    return resultado