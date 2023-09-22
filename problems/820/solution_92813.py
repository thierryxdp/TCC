def posLetra(frase,letra,n):
    quant_letras=str.count(frase,letra)
    
    if n>quant_letras:
        return -1