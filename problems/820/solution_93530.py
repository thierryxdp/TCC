def posLetra(frase,letra,numero):
    '''Função que recebe uma string, uma letra e um número que indica a ocorrência desejada da letra
    e retorna a posição da string que aquela ocorrência da letra está. Caso  exista menos ocorrências da letra do que a ocorrência pedida, a função retorna -1.
    str,str,int->int'''
    i = 0
    posicao = 0
    x = 0
    while i < numero:
        posicao = str.find(frase[posicao:],letra)+1
        x += posicao
        1 += 1
    return x - 1