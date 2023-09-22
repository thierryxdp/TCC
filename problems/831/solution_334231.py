def lingua_p(palavra):
    vogais = 'aeiouAEIOU'
    lista=[]
    for i in palavra:
        if i in vogais:
            palavra = palavra[0:i.index()] +'p' + palavra[i.index():]
    return palavra