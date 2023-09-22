def posLetra(string,letra,i):
    ''' funcao recebe uma string e retorna em que posicao da string 
    a letra esta. caso essa letra nao esteja no index informado, ela retornara
    -1. str,str,int-->int'''
    i=0
    while i<len(string):
        if letra in string:
            return str.find(string,letra,i)