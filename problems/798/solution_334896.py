def freq_palavras(frases):
    letras = {[]}
    for i in frases:
        if i not in letras:
            list.append(i,letras)
            vezes_que_apareceu= frases.count(i)
            list.append(vezes_que_apareceu,letras)
    return letras