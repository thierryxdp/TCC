def inverte(frase):
    "Retorna a mesma frase na ordem inversa, sem letras maiúsculas e pontuação.str->str"
    x = str.split(frase, ".", ",", "?","!", "-")
    list.reverse(x)
    y = str.join(" ", x)
    return y