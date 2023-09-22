def posLetra(string,letra,num):
    '''
    funcao que recebe uma string, uma letra em string e
    um numero que indica a ocorrencia desejada da letra
    e retorna em qual posicao da string essa ocorrencia
    esta e, caso exista menos ocorrencias da letra que
    a ocorrencia pedida, a funcao retorna -1
    str,str,int->int
    '''
    x=0
    y=0
    z=0
    lista=list(string)
    while x<len(lista):
        if lista[y]==letra:
            z=z+1
            if z==num:
                return y

        x=x+1
        y=y+1

    return -1