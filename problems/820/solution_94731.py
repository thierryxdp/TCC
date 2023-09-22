def posLetra(frase,letra,ocorrencia):
    if letra!='a':
        ff=str.replace(frase,letra,'a',ocorrencia-1)
    else:
        ff=str.replace(frase,letra,'b',ocorrencia-1)
    return ff.find(letra)