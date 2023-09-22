def inverte(frase):
    """Dada uma frase, retorna outra frase que contenha as mesmas palavras da frase de entrada
    na ordem inversa, sem letras maiúsculas, e sem pontuação;
    str -> str"""
    frase_atualizada = frase.replace("_", " ").replace("-", " ").replace(",", "").replace(":", "").replace(";", "").replace(".", "").replace("!", "").replace("?", "").replace("...", "")
    frase_separada = frase_atualizada.split(" ")
    frase_invertida = frase_separada.reverse()
    frase_nova = frase_invertida.join(" ")
    return frase_nova