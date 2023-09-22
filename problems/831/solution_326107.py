def lingua_p(palavra):
    str.lower(palavra)
    posicao=0
    for posicao in range(len(palavra)):
        if palavra[posicao] in 'aeiouáàéíóúãâêô':
            posicao +=1
            palavra=str.replace(palavra,palavra[posicao],palavra[posicao]+'p'+palavra[posicao])
    return palavra