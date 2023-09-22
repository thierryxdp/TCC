def posLetra(palavra,letra,indice):
    if str.count(palavra,letra)<indice:
        return -1
    else:
        return str.find(palavra,letra,str.find(palavra,letra))