def lingua_p(palavra):
    str.lower(palavra)
    str.split(palavra)
    lista=str.split(palavra)
    posicao=0
    for posicao in range(len(palavra)):
        if lista[posicao] in 'aeiouáàéíóúãâêô':
            posicao +=1
            del lista[posicao]
            list.insert(lista,posicao,str(lista[posicao]+'p'+lista[posicao]))
            palavra=str.join(lista)
            return palavra