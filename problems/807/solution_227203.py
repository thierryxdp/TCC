def conta_frases(frase):
    fras=str.split(frase,"'.')
    fra=str.split(frase,'...')
    f=str.split(frase,'!')
    frase=f+fra+fras
    
    return len(frase)