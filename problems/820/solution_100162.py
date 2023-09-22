def posLetra(frase,letra,numero):
    indice=0
    numocorrencias=str.count(frase,letra)
    resposta=0
    if numero > numocorrencias:
        return -1
    while indice < len(frase):
        y=str.find(frase,letra,indice)
        
        if y==numero:
            return y
        indice= indice + 1