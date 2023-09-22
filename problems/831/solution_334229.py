def lingua_p(palavra):
    vogais = 'aeiouAEIOU'
    lista=[]
    for i in palavra:
        if palavra[i] in vogais:
            lista += palavra[i]
    return lista