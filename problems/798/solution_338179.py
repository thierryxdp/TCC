def freq_palavras(frase):
    '''dada a variante, ele recebe a string e transformaem um dicionario com a frequencia de que cada palavra aparece.str->dict.'''
    palavras = str.split(frase)
    dicionario={}
    for i in palavras:
        if i in dicionario:
            dicionario[i]+=1
        else:
            dicionario[i]=1
    return dicionario