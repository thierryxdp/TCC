def lingua_p(palavra):
    lista = []
    for i in palavra:
        if i == 'e':
            lista.append(i +'p'+ i)
        if i == 'i':
            lista.append(i +'p'+ i)
        if i == 'o':
            lista.append(i +'p'+ i)
        if i == 'u':
            lista.append(i +'p'+ i)
        if i == 'a':
            lista.append(i +'p'+ i)
        else:
            lista.append(i)
    return str.join('',lista)