def inverte(frase):
    frase1 = str.lower(frase)
    frase_fatiada = str.split(frase1)
    
    
    
    return frase_fatiada[-1:-len(frase_fatiada)-1:-1]