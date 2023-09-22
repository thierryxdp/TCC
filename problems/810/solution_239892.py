def inverte(frase):
    """Dada uma frase a função retorna uma outra frase que contenha as mesmas palavras da frase
    de entrada na ordem inversa, sem letras maiúsculas, e sem pontuação
    str -> str"""
    return str.lower(str.join(" ",str.split(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase, "-", " "), ",", " "), ":", " "), ";", " "), ".", " "), "!", " "), "?", " "), "...", " "))[::-1]))