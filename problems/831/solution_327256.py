def lingua_p(palavra:str) -> str:
    lista = list(palavra)
    x = 0
    for i in range(len(lista)):
        if lista[i+x] in 'aeiouAEIOU':
            list.insert(lista, i, 'p')
            list.insert(lista, i+1, lista[x])
        	x +=2
    return lista