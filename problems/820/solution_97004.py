def posLetra(string,letra,ocorrencia):
    '''Função que recebe uma string, uma letra e um número que indica a ocorrência desejada da letra.
    Retorna em que posição da string aquela ocorrência da letra está.
    Se existir menos ocorrências da letra do que pedido, irá retornar -1;
    str, str, int -> int'''
    posicao = []
    i = 0
    while i <len(string):
        if string[i] == letra:
            posicao = posicao + [i]
        i=i+1
    return posicao[ocorrencia-1]