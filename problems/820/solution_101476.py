def posLetra(frase,letra,num):
    posicao=0
    indice=-1
    if num == (str.count(frase,letra)):
        return frase.rfind(letra)
    while 0<num<frase:
        if posicao != num:
            indice=indice+1
        if frase[indice] == letra:
            posicao=posicao+1
    return indice
    elif not 0<num<=(str.count(frase,letra)):
            return -1