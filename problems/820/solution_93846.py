def posLetra(frase,letra,indice):
    pos=0
    while str.find(frase[pos:],letra)<indice:
        pos=pos+1
        return pos