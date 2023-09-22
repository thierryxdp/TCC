def lingua_p(palavra:str) -> str:
    lista = list(palavra)
    x = 0
    l = palavra[x]
    for i in palavra():
        if l == 'aeiouAEIOU':
            list.insert(lista, i, p)
            list.insert(lista, i+1, l)
            x +=1
    return list.join(lista)