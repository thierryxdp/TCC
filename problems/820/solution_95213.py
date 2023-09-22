def posLetra(frase, letra, n):
    i=0
    cont=0
    a=frase.find(letra,i)
    while a!=-1:
        if(a!=-1 and a==i):
            cont+=1
            if(cont==n):
                return a
        a=frase.find(letra,i)
        i+=1
    return a