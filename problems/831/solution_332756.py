def lingua_p(palavra):
    lista = []
    for x in palavra:
        if x == 'e':
            lista.append(x +'p'+ x)
        elif x == 'i':
            lista.append(x +'p'+ x)
        elif x == 'o':
            lista.append(x +'p'+ x)
        elif x == 'u':
            lista.append(x +'p'+ x)
        elif x == 'a':
            lista.append(x +'p'+ x)
        else:
            lista.append(x)
    return str.join('',lista)