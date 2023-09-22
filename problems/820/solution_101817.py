def posLetra(frase,letra,n):
    i=0
    reps=1
    indice=-1
    if n>str.count(frase,letra):
        indice=-1
    else:
        while reps<=n:
            i=str.find(frase[i:],letra)
            indice+=1+i
            reps+=1
    return indice