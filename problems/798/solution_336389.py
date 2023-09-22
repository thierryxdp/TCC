def freq_palavras(frases):
    '''dada uma ou varias frases, a funçao a seguir nos 
    devolve um dicionario na qual tem como termos chave
    as palavras e como resultado da chave o numero
    de veses que a respectiva palavra apareceu no texto
    str--->Dicionario'''
    fraseLista=frases.split(' ')
    dic={}
    i=0
    while i<len(fraseLista):
        if 0==0:
        	n=fraseLista.count(fraseLista[i])
        	dic[fraseLista[i]]=n
        i=i+1
    return dic