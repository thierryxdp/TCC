def repetidos(lista):
    """Função que recebe uma sequencia de numeros em uma lista, e conta quantas vezes
    um elemento é igual ao elemento anterior.
    list -> int"""
    lst = []
    i=1
    while i<len(lista):
        if lista[i-1] == lista[i]:
            list.append(lst,1)
        i=i+1
    return sum(lst)