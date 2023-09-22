def inverte(frase):
    
    frase2 = str.lower(frase)
    frase_fatiada = str.split(frase2)
    frase3 = frase_fatiada[-1:-len(frase_fatiada)-1:-1]
    
    
    return str.join(" ",frase3).replace(".", "  ").replace("!","  ")