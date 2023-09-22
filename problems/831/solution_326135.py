def lingua_p(palavra):
    str.lower(palavra)
    str.split(palavra)
    lista=str.split(palavra)
    posicao=0
    for posicao in range(len(palavra)):
        if lista[posicao] in 'aeiouáàéíóúãâêô':
            return lista