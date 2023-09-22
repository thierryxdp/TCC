def posLetra(frase,letra,numero):
    indice=0
    numocorrencias=str.count(frase,letra)
    resposta=0
    if numero > numocorrencias:
        return -1
    while indice < len(frase):
        y=str.find(frase,letra,indice)
        indice= indice + 1
        if y==numero:
            return indice