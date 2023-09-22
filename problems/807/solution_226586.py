def conta_frases(frase):
    frase.replace('?',',')
    frase.replace('!',',')
    frase.replace('...',',')
    frase.replace('.',',')
    frase.split()
    
    
    return len(frase)