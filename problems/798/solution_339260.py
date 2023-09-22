def freq_palavras(frases):
    '''funçao que recebe uma string e retorna um dicionario
    onde cada palavra dessa string é uma chave e tem como valor
    o numero de vezes que a palavra aparece; str->dict'''
    dicionario={}
    p=str.split(frases)
    for elem in p:
        x=list.count(p,elem)
        dicionario[elem]=x
    return dicionario