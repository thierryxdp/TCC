def posLetra(frase,letra,n):
    i=0
    reps=1
    indice=-1
    if n>str.count(frase,letra):
        return indice
    else:
        while reps<=n:
            i=str.find(frase,letra,i,)
            indice+=1+i
            reps+=1
        return indice