def inverte(frase):
    "entra uma frase e na saida ela sai invertida"
    print(frase)
    frase = nopont(frase)
    frase = frase.split()
    frase = frase[::-1]
    
    return(' '.join(frase))