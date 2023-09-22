def freq_palavras(frases):
    '''recebe uma string e retorna um dicionario, onde 
    cada palavra dessa string seja uma chave e tenha como 
    valor o numero de vezes que a palavra aparece
    str->dict'''
    dicionario={}
    frase=str.split(frases,' ')
    for palavra in frase:
        if palavra not in dicionario:
            valor=list.count(frase,palavra)
            dicionario[palavra]=valor
    return dicionario