def posLetra(frase,letra,n):
    res = [i for i in range(len(frase)) if frase.startswith(letra, i)]
    if n<res[0]:
        return -1
    else:
        return res[n-1]