def inverte(frase):
    
    frase1 = str.lower(frase)
    frase2 = frase1.replace("?"," ").replace("..."," ").replace("!"," ").replace("."," ").replace(","," ").replace("-"," ")
    frase_fatiada = str.split(frase2)
    frase3 = frase_fatiada[-1:-len(frase_fatiada)-1:-1]
    frase4 = str.join(" ",frase3)
    
    
    
    return frase5