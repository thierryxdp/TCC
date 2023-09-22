def posLetra(texto, busca, n):
    ''' funçao que recebe como entrada uma string,uma letra e um numero que indica 
    a ocorrencia desejada da letra e retorna a posiçao da string aquela ocorrencia
    da letra esta.
    str,str,int -> int'''
    pos = texto.find(busca)
    while pos >= 0 and n > 1:
        pos = texto.find(busca, pos + 1)
        n -= 1
    return pos