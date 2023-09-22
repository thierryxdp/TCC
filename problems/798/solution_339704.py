def freq_palavras(frases):
    lista = frases.split(' ')
    dic = dict()
    for palavra in lista:
        dic(palavra) = lista.count(palavra)
return dic