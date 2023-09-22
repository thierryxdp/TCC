def posLetra(frase,letra,num):
    numero=''
    i=0
    x=list(range(1,str.count(frase,letra)))
    while num <= int(x[i]):
        numeros = numeros + str.index(frase,letra,i)
        i=i+1
    y=numeros(::-1)
    return frase[y[0]]