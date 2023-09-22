def lingua_p(palavra):
    str.lower(palavra)
    palavra=str.split(palavra)
    posicao=0
    for posicao in range(len(palavra)):
        if palavra[posicao] in 'aeiouáàéíóúãâêô':
            posicao +=1
            return palavra