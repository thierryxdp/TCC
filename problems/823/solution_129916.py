def faltante(lista):
    """funcao que retorna o numero que falta em um intervalo numero de uma lista;
    list -> int"""

    lista.sort()
    #f
    i = 0
    n = lista[len(lista)-1]

    if lista == list(range(1,n)):
                     
        return n + 1