def posLetra(frase,letra,n):
    '''funcao que retorna em qual posicao da frase a letra se repete em relacao ao numero dado
    str,str,int->int'''
    repeticao=n=0
    letra=''
    while n<len(frase):
        if frase[n]+letra==0:
            str.count(frase,letra)
        n=n+1
    return n-frase