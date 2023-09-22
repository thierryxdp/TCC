def posLetra(frase,letra,n):
    quant_letras=str.count(frase,letra)
    
    if letra not in frase:
        return -1