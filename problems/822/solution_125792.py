def repetidos(lista):
    """
    Recebe uma lista de numeros e retorna o numero de vezes que um
    elemento da lista é igual ao anterior;
    list -> int
    """
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if lista[j] == lista[i]:
                lista = del(lista[j])
            else:
                j = j + 1
        i = i + 1
	lista = lista.sort()
    return len(lista)