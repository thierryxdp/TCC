def posLetra(frase,letra,indice):
    proximo=0
    pos=0
    while proximo<len(frase):
        if str.find(3[pos:],letra)>indice:
            pos=pos+1
        return pos