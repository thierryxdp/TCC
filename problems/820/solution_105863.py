def posLetra(string,letra,x):
    '''funcao recebe uma string e retorna em que a letra esta. caso essa
    letra nao esteja no inteiro -1. str, str, int-->int'''
    i=x
    loc=0
    while i!=0:
        loc = loc + str.find(string,letra,loc): loc
        i= i-1
    return loc-1