def inverte(frase):
    frase1 = str.lower(frase)
    frase_fatiada = str.split(frase1)
    frase3 = frase_fatiada[-1:-len(frase_fatiada)-1:-1]
    frase4 = frases3.replace("?","/").replace("...","/").replace("!","/").replace(".","/")
    
    return str.join(" ",frase3)