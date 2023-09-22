def posLetra(frase,letra,num):
    i=0
    x=str.count(frase,letra)
    if (num < x):
        return str.index(str.find(frase,letra,num))