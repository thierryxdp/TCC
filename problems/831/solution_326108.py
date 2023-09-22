def lingua_p(palavra):
    str.lower(palavra)
    posicao=0
    for posicao in range(len(palavra)):
        if palavra[posicao] in 'aeiouáàéíóúãâêô':
            posicao +=1
            palavra=str.replace(palavra,palavra[posicao],str(palavra[posicao])+str(p)+str(palavra[posicao]))
    return palavra