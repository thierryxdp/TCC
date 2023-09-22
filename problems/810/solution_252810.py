def inverte(frase):
    frase = retira.pontuacao(frase)
    frase = frase.lower()
    frase = frase.split()
    frase.reverse()
    frase = " ".join(frase)
    
    return(frase)