def inverte(frase):
    "entra uma frase e na saida ela sai invertida"
    frase = frase.split()
    frase = frase[::-1]
    
    return(' '.join(frase))