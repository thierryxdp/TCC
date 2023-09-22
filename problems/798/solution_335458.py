def freq_palavras(frases):
    '''recebe uma string e retorna um dicionario, onde 
    as chaves sao palavras dessa string e os valores 
    são os numeros de vezes que a palavra aparece
    str->dict'''
    dicionario={}
    frase=str.split(frases,' ')
    for palavra in frase:
        if palavra not in dicionario:
            valor=str.count(frases,palavra)
            dicionario[palavra]=valor
    return dicionario