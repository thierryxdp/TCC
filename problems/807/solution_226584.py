def conta_frases(frase):
    frase.replace('?',',')
    frase.replace('!',',')
    frase.replaec('...',',')
    frase.replace('.',',')
    
    
    return len(frase)