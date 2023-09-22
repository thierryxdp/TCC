def posLetra(string,letra,indice):
    quant=0
    contador=0
    if indice > string.count(letra):
        return -1
    else:
        while contador<string.count(letra):
            quant+=1          
            contador+=1
        return quant