def posLetra(frase,letra,n):
    '''funcao que retorna em qual posicao da frase a letra se repete em relacao ao numero dado
    str,str,int->int'''
    i=0
    letra=0
    while n<len(frase):
        if frase[i]+letra==0:
            str.count(frase,letra)
        i=i+1
    return letra