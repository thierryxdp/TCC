def lingua_p(palavra):
    str.lower(palavra)
    str.split(palavra)
    lista=str.split(palavra)
    posicao=0
    for posicao in range(len(palavra)):
        vogal=lista[posicao]
        if vogal in 'aeiouáàéíóúãâêô':
            posicao +=1
            del vogal
            list.insert(lista,posicao,str(vogal+'p'+vogal))
            palavra=str.join(lista)
            
            
            return palavra