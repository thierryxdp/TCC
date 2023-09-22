def posLetra(frase,letra,n):
    '''Recebe uma string, uma letra e um numero indicando a ocorencia desejada
    da letra e retorna a posicao da string em que aquela ocorrencia da letra
    se encontra;
    str,str,int->int'''
    i=n
    posicao=0
    while i!=0:
        posicao = posicao+ (str.find(frase,letra,posicao))
        i=i-1
    return posicao-1