def faltante(lista):
    """A função retorna um número inteiro x que pertence ao intervalo
    [1,N] mas que não pertence a lista de entrada L.
    list-->int."""
    list.sort(lista)
    i = 1
    while i <= len(lista)+1:
        if i not in lista:
            return i
        i +=1