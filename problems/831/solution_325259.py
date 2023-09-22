def lingua_p(palavra):
    """Este código recebe uma palavra e retorna a mesma palavra com
    a letra 'p' após cada vogal, seguido da vogal anterior.
    Recebe: str
    Retorna str"""
    novapalavra = ''
    posicao = 0
    
    while posicao < len(palavra):
        if palavra[posicao] in 'aeiouAEIOU':
            novapalavra = novapalavra + palavra[posicao] + 'p' + palavra[posicao]
        if palavra[posicao] not in 'aeiouAEIOU':
            novapalavra = novapalavra + palavra[posicao]
        posicao = posicao + 1
    return novapalavra