retira_pontuacao (frase):
    """funcao que substitue os caracteres por espacos
    str -> str"""
    for caracteres in "-,:;,.~^*&"%$@?!":
        frase = frase.replace(caracteres," "):
    return frase