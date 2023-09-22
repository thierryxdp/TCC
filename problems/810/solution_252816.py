def inverte(frase):
    frase = frase.retira_pontuacao ()
    frase = frase.lower()
    frase = frase.split()
    frase.reverse()
    frase = " ".join(frase)
    
    return(frase)