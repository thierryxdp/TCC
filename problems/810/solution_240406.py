def inverte(frase):
    
    frase.replace("!"," ").replace("?"," ").replace("."," ").replace(";"," ").replace("-"," ").replace(":"," ").replace(","," ")
    
    str.split(frase, ' ')
    
    frase.reverse()
    
    str.join(' ',frase)
    
    return frase