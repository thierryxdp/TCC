def posLetra(string,letra,numero):
    '''Função que recebe uma string, uma letra e um número que indica a ocorrência desejada da letra
    e retorna a posição da string que aquela ocorrência da letra está. Caso  exista menos ocorrências da letra do que a ocorrência pedida, a função retorna -1.
    str,str,int->int'''
    lista = list(string)
    contagem = 0
    posicao = 0
    
       	while contagem != numero:
            if lista(posicao) == letra:
                contagem = contagem + 1
                posicao = posicao + 1
                return posicao - 1
            else:
                return -1