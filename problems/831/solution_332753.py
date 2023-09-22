def lingua_p(palavra):
    lista = []
    for x in palavra:
        if x == 'e':
            lista.append(x +'p'+ x)
        if x == 'i':
            lista.append(x +'p'+ x)
        if x == 'o':
            lista.append(x +'p'+ x)
        if x == 'u':
            lista.append(x +'p'+ x)
        if x == 'a':
            lista.append(x +'p'+ x)
        else:
            lista.append(x)
    return str.join('',lista)