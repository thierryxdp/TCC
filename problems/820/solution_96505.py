def posLetra(texto,letra,ocorrencia):
    '''função que retorna em que posição da string a ocorrência
    da letra está no texto
    str, str, int -> int'''
    cont = 0
    posicao = ''
    while cont < ocorrencia:
        posicao = str.find(texto,letra,cont)
        cont += 1
    return posicao