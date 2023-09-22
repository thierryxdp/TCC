def posLetra(string,letra,indice):
    quant=0
    count=string.count(letra)
    contador=0
    if indice > count:
        return -1
    else:
        while contador<string.count(letra):
            quant+=1          
            contador+=1
        return quant