def inverte(frase):
    frase0 = frase.repalce("-","/").replace(".","/").replace("!","/").replace(",","/")
    frase1 = str.lower(frase0)
    frase_fatiada = str.split(frase1)
    frase3 = frase_fatiada[-1:-len(frase_fatiada)-1:-1]
    
    
    return str.join(" ",frase3)