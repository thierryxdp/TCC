def inverte(frase):
    "entra uma frase e na saida ela sai invertida"
    frase = frase.replace(',','').replace('.','').replace(';','').replace('-','').replace(':','').lower()
    frase = frase.split()
    frase = frase[::-1]
    
    return(' '.join(frase))