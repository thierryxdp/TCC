def inverte_frase(texto):
    """Dado uma frase, retorna ela na ordem inversa, sem letras
    maiúsculas e sem pontuação."""
    
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