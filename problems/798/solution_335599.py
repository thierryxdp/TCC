def freq_palavras(frases):
    '''função que recebe uma strig e retorna um dicionario onde cada palavra dessa string é uma chave que esta associada ao valor que corresponde a quantas vezes essa palavra aparece na string;string->dict'''
    dicionario={}
    palavras=str.split(frases)
    for i in palavras:
        dicionario[i]=list.count(palavras,i) 
    return dicionario