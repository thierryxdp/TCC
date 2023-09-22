def lingua_p(palavra):
    str.lower(palavra)
    posicao=0
    for posicao < range(len(palavra)):
        vogal=letra[posicao]
        if vogal in 'aeiouáàéíóúãâêô':
            palavra=str.replace(palavra, vogal, vogal +'p'+ vogal)
    return palavra