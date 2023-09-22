def repetidos(lista):
    "Retorna o numero de vezes que um elemento da lista é igual ao elemento anterior. list->int"
    i = 0
    lista_nova = []
    while i<=len(lista):
        if lista[i] == lista[i-1]:
            lista_nova.append(1)
        i+=1
    return len(lista_nova)