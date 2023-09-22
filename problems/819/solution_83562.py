def filtraMultiplos(numeros,n):
    t=tuple()
    i= 0
    while i<= len(numeros):
        if (numeros[i]%n) ==0:
            t = t+(numeros[i],)
        i+=1    
    return t