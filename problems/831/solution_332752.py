def lingua_p(palavra):
    lista = []
    for x in palavra:
        if x == 'e':
            lista.append(i +'p'+ i)
        if x == 'i':
            lista.append(i +'p'+ i)
        if x == 'o':
            lista.append(i +'p'+ i)
        if x == 'u':
            lista.append(i +'p'+ i)
        if x == 'a':
            lista.append(i +'p'+ i)
        else:
            lista.append(x)
    return str.join('',lista)