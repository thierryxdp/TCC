def posLetra(texto, letra, n):
    '''Função recebe como entrada uma string, uma letra, e um número que indica a ocorrência desejada da letra que retorna em que posição da string aquela ocorrência da letra está.
    string,string,int->int'''
    posicao = texto.find(letra)
    while posicao >= 0 and n > 1:
        posicao = texto.find(letra, posicao + 1)
        n -= 1
    return posicao