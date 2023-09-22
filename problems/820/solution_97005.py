def posLetra(string,letra,ocorrencia):
    '''Função que recebe uma string, uma letra e um número que indica a ocorrência desejada da letra.
    Retorna em que posição da string aquela ocorrência da letra está.
    Se existir menos ocorrências da letra do que pedido, irá retornar -1;
    str, str, int -> int'''
    posicao = string.find(letra)
    while posicao >= 0 and ocorrencia > 1:
        posicao = string.find(letra, posicao + 1)
        ocorrencia -= 1
    return posicao