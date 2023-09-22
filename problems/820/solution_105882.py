def posLetra(string,letra,posi):
    encontra = string.find(letra)
    while encontra >=0 and posi>1:
        encontra = string.find(letra, encontra+1)
        posi = posi-1
    return encontra