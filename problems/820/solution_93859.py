def posLetra(frase,letra,indice):
    proximo=0
    pos=0
    while proximo<len(frase):
        if str.find(frase[pos:],letra)==indice:
            pos=pos+1
        else:
            return -1
        return pos