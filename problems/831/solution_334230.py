def lingua_p(palavra):
    vogais = 'aeiouAEIOU'
    lista=[]
    for i in palavra:
        if i in vogais:
            lista += i
    return lista