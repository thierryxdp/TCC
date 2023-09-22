def freq_palavras(frases):
    '''Esta função recebe uma string de uma frase e retorna um dicionário, onde cada palavra é uma chave e a sua frequência, o valor.
str->dict'''
    i=0
    lista=[]
    frequencia=0
    d1={}
    lista=str.split(frases,' ')
    for i in range(len(lista)):
        d1=dict([(lista[i],[])])
        d1[lista[i]].append(list.count(lista,lista[i]))
    return d1