def conta_frases(frase):
    """ funçao que analisa as pontuacoes
        :srt --> int """
    frase1 = frase.replace("...", "!")
    frase2 = frase1.replace("?", "!")
    frase3 = frase2.replace(".", "!")
    return len(frase3.split("!"))-1