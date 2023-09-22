def inverte(frase):
    """Esta função retorna uma frase ao contrário, porém, sem letras maiúsculas e sem pontuação."""
    x1 = pontuacao(frase)
    x2 = str.lower(x1)
    x3 = str.split(x2, " ")
    x4 = x3[::-1]
    x5 = str.join(" ",x4)
    return x5