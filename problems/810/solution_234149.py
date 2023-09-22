def inverte(texto):
    lista = []
    for i in texto:
        if i not in ':;.,-!?':
            lista.append(i.lower())
        elif i in ':;.,-!?':
            lista.append(' ')
    frase = str.split(str.join('', lista), ' ')
    return str.join(' ', frase[::-1])