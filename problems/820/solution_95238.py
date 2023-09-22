def posLetra(string,letra,numero):
    i = 0
    contagem = 0
    if strig.count(letra)>=numero:
        while contagem != numero:
            if letra == string[i]:
                contagem+=1
            i = i + 1
        return i - 1
     else:
        return -1