def freq_palavras(frases):
    '''Função que recebe uma string e retorne um dicionario onde cada palavra
    dessa string seja uma chave e tenha como valor o numero de vezes que a palavra aparece
    str->dict'''
    d = {}
    x= str.split(frases)
    for elem in x:
        y=list.count(x,elem)
        d[elem]= y
    return d