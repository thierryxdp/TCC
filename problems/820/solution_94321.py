def posLetra(string,letra,numero):
    '''Função que recebe uma string, uma letra e um número que indica a ocorrência desejada da letra
    e retorna a posição da string que aquela ocorrência da letra está. Caso  exista menos ocorrências da letra do que a ocorrência pedida, a função retorna -1.
    str,str,int->int'''
    lista = list(string)
    posicao = 0
    ocorrencia = 0
    tamanho = len(lista)
    
    while posicao != tamanho:
    	if lista[posicao] == letra and ocorrencia == numero - 1:
            return posicao
        elif lista[posicao] == letra:
            posicao = posicao + 1
            ocorrencia = ocorrencia + 1
        else:
            posicao = posicao + 1
    return -1