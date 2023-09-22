def inverte(frase):
    """Funcao que dada uma frase(string) retorna uma outra drase que contem as
    palavras da frase de entrada na ordem inversa, sem letras maiusculas e sem
    pontuacao."""
    frase = semPontuacao(frase)
    frase = frase.lower()
    frase = str.split(frase)
    inversao = frase[::-1]
    juncao = " ".join(inversao) 
    return juncao