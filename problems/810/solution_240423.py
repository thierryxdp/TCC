def inverte(frase):
    
    sempont=frase.replace("!"," ").replace("?"," ").replace("."," ").replace(";"," ").replace("-"," ").replace(":"," ").replace(","," ")
    
    frasenova= sempont.split()
    
    invertida = frasenova[::-1]
    
    frasenv = str.join(' ',invertida)
    
    return frasenv.lower