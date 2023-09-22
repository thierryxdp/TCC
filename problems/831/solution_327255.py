def lingua_p(palavra:str) -> str:
    lista = list(palavra)
    x = 0
    for i in lista:
        if lista[x] in 'aeiouAEIOU':
            list.insert(lista, x, 'p')
            list.insert(lista, x+1, lista[x])
        x +=1
    return lista