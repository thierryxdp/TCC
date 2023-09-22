def lingua_p(palavra):
    lista = []
    for i in palavra:
        if palavra == ('a','e','i','o','u'):
            lista.append(i,'p')
        else:
            lista.append(i)
    return str.join(lista)