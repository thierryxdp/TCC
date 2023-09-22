def filtraMultiplos(numeros, n):
    listaNum=[]
    i=0
    while i < len(numeros):
        if numeros[i]%n==0:
            listaNum.append(numeros[i])
        i=i+1
        return listaNum