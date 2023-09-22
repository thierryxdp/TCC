def conta_frases(frase):
    frase=str.split(frase,"'.')
    frase=str.split(frase,'...')
    frase=str.split(frase,'!')
    teste=[]
    final= teste + frase
    
    
    return len(final)