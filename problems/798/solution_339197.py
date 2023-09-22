def freq_palavras(frases):
    '''funcao que recebe uma string e retorna um dicionario onde cada palavra dessa string seja uma chave e tenha como valor o numero de vezes que a palavra aparece
    str->dict'''
    n={}
    stringF=str.split(frases)
    for x in stringF:
        if not x in n:
            n[x]=list.count(stringF,x)
    return n