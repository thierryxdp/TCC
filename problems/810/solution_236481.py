def frase(texto):
    """Dado uma frase, substitui toda a pontuação dela por espaço."""
    
    frase = texto.replace("?", " ")
    frase = frase.replace("!", " ")
    frase = frase.replace(",", " ")
    frase = frase.replace(".", " ")
    frase = frase.replace(":", " ")
    frase = frase.replace(";", " ")
    frase = frase.replace("-", " ")
    frase = frase.replace("...", " ")
    
    frase = str.lower(frase)
    
    palavras = frase.split()
    palavras = palavras[::-1]
    reversa = str.join(" ", palavras)
    
    return reversa