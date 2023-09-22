#Questão 3
def posLetra(frase,letra,ocorrencia):
    '''Retorna em que posição da frase a ocorrência da letra está
str,str,int -> int'''
    if str.count(frase,letra)<ocorrencia:
        return -1
    contador=0
    i=0
    while contador<ocorrencia and i<len(frase):
        if frase[i]==letra:
            contador=contador+1
        i=i+1
    return i