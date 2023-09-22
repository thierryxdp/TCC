def inverte (frase):
    
    frase = retira_pontuacao(frase)
    
    frase = frase.lower()
    
    frase = frase.split()
    
    frase.reverse()
    
    frase = " ".join(frase)
    
    return (frase)