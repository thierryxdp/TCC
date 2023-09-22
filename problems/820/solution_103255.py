def posLetra(string,letra,n):
    '''funcao que retorna em qual posicao da frase a letra se repete em relacao ao numero dado
    str,str,int->int'''
    i=0
    letra=0
    while n<len(string):
        if string[i] in letra:
            letra=letra+1
        if letra==n:
        i=i+1
            return i
        if letra<n:
            return -1