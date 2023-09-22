def faltante(lista):
    i=0
    resultado=1
    while i<len(lista):
        x=list(range(1,lista[-1]+1))
        if x[i]==lista[i]:
            resultado+=1
        i=i+1
    return resultado