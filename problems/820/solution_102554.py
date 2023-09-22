def posLetra(frase,letra,n):
    if letra in frase:
        res = [i for i in range(len(frase)) if frase.startswith(letra, i)]
        return res[n-1]
    else:
        return -1