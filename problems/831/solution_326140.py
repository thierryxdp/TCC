def lingua_p(palavra):
    str.lower(palavra)
    str.split(palavra)
    lista=str.split(palavra)
    posicao=0
    for posicao in len(lista):
        if lista[posicao] in 'aeiouáàéíóúãâêô':