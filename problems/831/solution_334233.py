def lingua_p(palavra):
    vogais = 'aeiouáéíóúàèìòù'
    lista=[]
    p = str.lower(palavra)
    for i in p:
        if i in vogais:
            lista.append(i +'p' + i)
        else:
            lista.append(i)
    return ''.join(lista)