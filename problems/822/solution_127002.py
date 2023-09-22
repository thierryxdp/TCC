def repetidos(lista):
    """A função recebe como entrada uma lista de inteiros
    e retorna um int informando quantas vezes um elemento 
    da lista é igual ao elemento anterior."""
    vezes = 0
    i = 1
    while i < len(lista):
        if lista[i] == lista[i-1]:
            vezes += 1
            i += 1
        else:
            i += 1
    return vezes