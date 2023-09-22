def freq_palavras(frases):
    '''Recebe uma string e retorna dicionario onde cada
    palavra dessa string seja uma chave e tenha como valor
    o numero de vezes que a palavra aparece'''
    '''str->dict'''
    palavras=frases.split()
    dic=()
    for i in palavras:
        cont=palavras.count(i)
        dic.update(cont)
    return dic