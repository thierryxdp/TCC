def posLetra(frase,letra,n):
    res = [i for i in range(len(frase)) if frase.startswith(letra, i)]
    return res[n-1]