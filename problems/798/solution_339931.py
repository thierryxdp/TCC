def freq_palavras(frases):
    frases=frases.split()
    lista = {}
    for palavra in frases:     
        if palavra not in lista:
            lista[palavra] = 1
        else :
            lista[palavra] +=1
    return lista
freq_palavras("O rato roeu")