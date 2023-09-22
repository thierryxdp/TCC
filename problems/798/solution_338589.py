def freq_palavras(frases):
    '''Essa função recebe uma string e retorna um dicionário com as 
    palavras dessa string e o número de vezes que a palavra aparece,
    str->dict'''
    i=0
    frase1=str.split(frases)
    for x in frase1:
        if x==frase1[i]:
           frasef={x:frase1.count(x)}
        i+=0
        frasef[x]=frase1.count(x)
    return frasef