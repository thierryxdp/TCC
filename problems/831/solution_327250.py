def lingua_p(palavra:str) -> str:
    lista = list(palavra)
    for i in lista:
        x = 0
        if lista[x] == 'aeiouAEIOU':
            list.insert(lista, i, p)
            list.insert(lista, i+1, l)
            x +=1
    return lista