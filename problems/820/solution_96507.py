def posLetra(texto,letra,ocorrencia):
    '''função que retorna em que posição da string a ocorrência
    da letra está no texto
    str, str, int -> int'''
    cont = 1
    posicao = ''
    while cont < ocorrencia:
        cont += 1
        posicao = str.find(texto,letra,cont)
    return posicao