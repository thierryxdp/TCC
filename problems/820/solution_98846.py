def posLetra(palavra,letra,indice):
x=str.find(palavra,letra)
    if str.count(palavra,letra)<indice:
        return -1
    else:
        return str.find(palavra,letra,x)