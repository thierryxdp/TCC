def posLetra (string, letra,numero):
    i=0
    contagem = 0
    if string.count(letra) >=numero:
        whle contagem != numero:
            if letra == string[i]:
                contagem +=1
            i+=1
        return i-1
    else:
        return -1