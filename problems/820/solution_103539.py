def posLetra(frase,letra,n):
    '''funcao que retorna em qual posicao da frase a letra se repete em relacao ao numero dado
    str,str,int->int'''
    i=0
    acumulador=0
    while i<len(frase):
            posicao=str.find(frase,letra)
            acumulador=acumulador+posicao
            i=i+1
        return acumulador