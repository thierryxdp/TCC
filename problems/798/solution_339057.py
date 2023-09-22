def freq_palavras(frases):
    '''Essa função recebe uma string e retorna um dicionário com as 
    palavras dessa string e o número de vezes que a palavra aparece,
    str->dict'''
    dicionario=dict()
    frase1=str.split(frases)
    for x in frase1:
        if x in frase1:
           dicionario[x]=1
    return dicionario