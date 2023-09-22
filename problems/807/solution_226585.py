def conta_frases(frase):
    frase.replace('?',',')
    frase.replace('!',',')
    frase.replace('...',',')
    frase.replace('.',',')
    
    
    return len(frase)