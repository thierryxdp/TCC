def posLetra(frase,letra,n):
    '''Função que recebe uma string,uma letra e um número que indica a ocorrência desejada da letra, e retorna em que posição da string aquela ocorrência da çetra está;
    str,str,int->int'''
    posicao = 0
    ocorrencia = 0
    proximo = 0
    while ocorrencia < n:
        posicao = str.find(frase,letra,proximo)
        proximo = posicao + 1
        ocorrencia = ocorrencia + 1
    return posicao