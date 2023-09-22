def filtraMultiplos (lista, n):
    """Retorna os múltiplos de um número de entrada "n"; list, int -> list"""
    contador= 0
    multiplo= []
    while  contador < len(lista):
        if lista [contador] % n == 0:
            multiplo = multiplo + [lista[contador]]
        contador =  contador + 1
    return multiplo