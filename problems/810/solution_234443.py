def inverte(frase):
    change= " "
    frase0 = change.join(frase)
    frase1 = frase0.repalce("-","/").replace(".","/").replace("!","/").replace(",","/")
    frase2 = str.lower(frase1)
    frase_fatiada = str.split(frase2)
    frase3 = frase_fatiada[-1:-len(frase_fatiada)-1:-1]
    
    
    return str.join(" ",frase3)