def posLetra(string,letra,ocorrencia):
    '''Dado uma string,uma letra e um numero que indica a ocorrencia desejada da letra,retorna
    em que posição da string a determinada ocorrencia da letra está. Caso exista menos ocorrencias
    da letra do que a ocorrencia pedida, retorna -1.str,str,int->int'''
    a=0
    b=0
    while a<len(string) and b<ocorrencia:
        if string[a]==letra:
            b=b+1
        a=a+1
    if b<ocorrencia:
        return -1
    else:
        return a-1