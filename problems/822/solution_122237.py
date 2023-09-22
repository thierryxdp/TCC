def repetidos(lista):
    """retorna o numero de vezes que o elemento 
    da lista dada e igual ao elemento anterior """
    atual = []
    proximo = []
    cont = 1
    repetido = 0
    for i in lista:
        if cont < len(lista):
            proximo = lista[cont]
            atual = i
            if atual == proximo:
                repetido += 1
            cont += 1
    return repetido