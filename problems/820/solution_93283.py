def posLetra(string,l,n):
    '''uma função que retorna em que posição da string aquela ocorrência da letra está
    Caso exista menos ocorrências da letra do que a ocorrência pedida, a função 
    deve retornar -1.
    str + str + int ->'''
    posicao = 0
    encontrados =0 
    atual = ''
    if n > str.count(string, l):
        return -1
    while posicao < len(string) and encontrados < n:
        atual = string[posicao]
        if atual == l:
            encontrados += 1
        posicao += 1
    if encontrados == n:
        return posicao -1