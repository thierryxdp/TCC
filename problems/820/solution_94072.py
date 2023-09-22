def posLetra(frase,letra,n):
    '''função que recebe como entrada uma string,uma letra e um numero, e retorna em que possição da string,aquela ocorrência da letra esta; str,int->int'''
    frase15 = str.replace(frase,letra,'+',n-1)
    return str.find(frase15,letra)