def lingua_p(palavra):
    lista = []
    for i in palavra:
        if i == 'e':
            lista.append(i +'p')
        if i == 'i':
            lista.append(i +'p')
        if i == 'o':
            lista.append(i +'p')
        if i == 'u':
            lista.append(i +'p')
        if i == 'a':
            lista.append(i +'p')
        else:
            lista.append(i)
    return str.join('',lista)