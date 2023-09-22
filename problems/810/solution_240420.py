def inverte(frase):
    
    sempont=frase.replace("!"," ").replace("?"," ").replace("."," ").replace(";"," ").replace("-"," ").replace(":"," ").replace(","," ")
    
    frasenova= sempont.split()
    
    invertida = frasenova[::-1]
    
    return invertida