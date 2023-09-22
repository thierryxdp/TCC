def inverte(frase):
    frase1 = frase.replace("?","/").replace("...","/").replace("!","/").replace(".","/")
    frase2 = frase1.split("/")
    frase_fatiada = str.split(frase2)
    
    
    
    return frase_fatiada[-1:-len(frase_fatiada)-1:-1]