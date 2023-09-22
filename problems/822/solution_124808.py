def repetidos(lista:list)->int:
    vezes = 0
    count = 1
    while count < len(lista):
        if lista[count] == lista[count-1]:
            vezes += 1
        count += 1
    return vezes