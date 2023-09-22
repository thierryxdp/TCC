def inverte(frase):
    """Essa função recebe uma frase, remove sua pontação e inverte ela.
    entrada: string, saída: string"""
    
    frase = retira_pontuacao(frase)
    
    frase = frase.lower()
    
    frase = frase.split()
    
    frase.reverse()
    
    frase = " ".join(frase)
    
    return(frase)