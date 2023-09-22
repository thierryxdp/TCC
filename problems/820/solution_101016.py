def posLetra(texto,letra,n):
    '''funcao que indica a ocorrencia da letra desejada dentro de uma string; str,str,int -> int'''
    posicao = texto.find(letra)
    while posicao >= 0 and n > 1:
        posicao = texto.find(letra,posicao + 1)
        n = n + 1
    return posicao