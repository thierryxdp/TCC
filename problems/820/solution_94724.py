def posLetra(frase,letra,ocorrencia):
    if letra!='a':
        str.replace(frase,letra,'a',ocorrencia-1)
    else:
        str.replace(frase,letra,'b',ocorrencia-1)
    return frase.find(letra)