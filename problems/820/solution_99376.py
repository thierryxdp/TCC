def posLetra(string,letra,num):
    '''funcao que recebe uma string, uma letra e o numero de ocorrencia da letra desejada e retorna a posicao da lista na qual a ocorrencia dessa letra aconteceu;
       str,str,int->int'''
    acumulador=[]
    i=0
    while i<len(string):
        if letra in string[i]:
            acumulador=acumulador+[i,]
        i=i+1
    posicao=num-1
    if len(acumulador)<num:
        return -1
    else:
        return acumulador[posicao]