def inverte(frase):
    "Retorna a mesma frase na ordem inversa, sem letras maiúsculas e pontuação.str->str"
    frase1 = str.split(frase,".")
    juntaf = str.join(" ", frase1)
    return juntaf[::-1]