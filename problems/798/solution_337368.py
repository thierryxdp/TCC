def freq_palavras(frases):
    '''Esta função recebe uma string de uma frase e retorna um dicionário, onde cada palavra é uma chave e a sua frequência, o valor.
str->dict'''
    d1_repete={}
    lista=str.split(frases,' ')
    for palavra in lista:
        repeticao=list.count(lista,palavra)
        d1_repete[palavra]=repeticao
    return d1_repete