def posLetra(string,letra,x):
    ''' funcao que recebera uma string , uma letra e um numero. e que retornara na posição em que a steing da letra esta.
    str,str,int-->int'''
    i=x
    loc=0
    while i!=0:
        loc = loc + str.find(string,letra,loc)
        i= i-1
    return loc-1