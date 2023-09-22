def posLetra(frase,letra,n):
    quant_letras=str.count(frase,letra)
    
    if letra not in frase or n>quant_letras:
        return -1