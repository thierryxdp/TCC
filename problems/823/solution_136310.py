def faltante(lista):
    """Função que verifica o número entre as listas que estão faltando"""
    """list -> int"""
    i = 0
    while i < (len(lista) + 1):
        if (i + 1) > len(lista):
            return i + 1
        elif (i + 1) != lista[i]:
            return lista[i] - 1
        i += 1