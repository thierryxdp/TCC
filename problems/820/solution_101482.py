def posLetra(frase,letra,num):
    contagem=str.count(frase,letra)
    posicao=0
    indice=-1
    if num == contagem:
        return frase.rfind(letra)
    elif 0<num<frase:
        while posicao != num:
            indice=indice+1
            if frase[indice] == letra:
                posicao=posicao+1
        return indice
    elif not 0<num<=contagem:
        return -1