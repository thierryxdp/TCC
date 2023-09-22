def lingua_p(palavra):
    lista = list(palavra)
    for x in lista:
        if x == 'a' or x == 'e' or x == 'i' or x == 'i' or x == 'o' or x == 'u':
            y = x.index
            list.insert('p', y-1)
            list.insert('p', y+1)
    return str(lista)