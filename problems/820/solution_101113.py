def posLetra(string,letra,x):
    ''' funcao recebe uma string e retorna em que posicao da string 
    a letra esta. caso essa letra nao esteja no index informado, ela retornara
    -1. str,str,int-->int'''
    i=x
    loc=0
    while i!=0:
        loc = loc + str.find(string,letra,loc)- loc+1
        i= i-1
    return loc-1