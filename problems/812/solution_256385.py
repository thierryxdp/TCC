def retira_pontuacao(texto):
    """Dado uma frase, substitui toda a pontuação dela por espaço."""
    
    frase = texto.replace("?", " ")
    frase = frase.replace("!", " ")
    frase = frase.replace(",", " ")
    frase = frase.replace(".", " ")
    frase = frase.replace(":", " ")
    frase = frase.replace(";", " ")
    frase = frase.replace("_", " ")
    frase = frase.replace("...", " ")
    
    return texto