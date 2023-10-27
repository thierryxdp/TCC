def freq_palavras(frase):
    dic = {}
    lista = frase.split()
    for palavra in lista:
        if palavra in dic:
            dic[palavra] += 1
        else:
            dic[palavra] = 1
    return dic
