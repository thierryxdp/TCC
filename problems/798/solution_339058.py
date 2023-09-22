def freq_palavras(frases):
    '''Essa função recebe uma string e retorna um dicionário com as 
    palavras dessa string e o número de vezes que a palavra aparece,
    str->dict'''
    dicionario=dict()
    frase1=str.split(frases)
    for x in frase1:
        if x not in dicionario:
           dicionario[x]=1
        else:
          dicionario[x]+=1
    return dicionario