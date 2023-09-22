def posLetra(frase,letra,x):
    '''Recebe uma string, uma letra e um numero indicando a ocorencia desejada
    da letra e retorna a posicao da string em que aquela ocorrencia da letra
    se encontra;
    str,str,int->int'''
    i=x
    loc=0
    while i!=0:
        loc = loc + str.find(frase,letra,loc)
        i= i-1
    return loc-1