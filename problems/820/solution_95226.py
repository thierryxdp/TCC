def (string,letra,n):
    i = 0
    contagem = 0
    if strig.count(letra)>=n:
        while contagem != n:
            if letra == string[i]:
                contagem+=1
            i = i + 1
        return i - 1
     else:
        return -1