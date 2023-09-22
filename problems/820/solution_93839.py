def posLetra(frase, letra, n):
    frase2=str.replace(frase,letra, '+', n-1)
    return str.find(frase2, letra)