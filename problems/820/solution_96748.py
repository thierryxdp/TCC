def posLetra(texto, busca, n):
    '''Rece uma str como entrada e indica a ocorrencia desejada
    str-->str'''
    pos = texto.find(busca)
    while pos >= 0 and n > 1:
        pos = texto.find(busca, pos + 1)
        n = n -  1
    return pos