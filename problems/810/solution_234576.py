def inverte(frase):
    """fauncao que dada uma frase retorne uma outra frase que contenha
    as mesmas palavras da frase de entrada na ordem inversa sem letras maiusculas e sem pontuacao
    string"""
    frase1 = str.replace(frase, "-", " ")
    frase2 = str.replace(frase1, ",", " ")
    frase3 = str.replace(frase2, "...", " ")
    frase4 = str.replace(frase3, "..", " ")
    frase5 = str.replace(frase4, ";", " ")
    frase6 = str.replace(frase5, "!", " ")
    frase7 = str.replace(frase6, "?", " ")
    frase  = str.lower(frase7)
    frase nova = str.split(frase, " ")
    frase nova2 = frase_nova[::-1]
    string = " ".join(frase_nova)
    return string