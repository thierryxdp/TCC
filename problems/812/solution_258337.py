def retira_pontuacao (frase):
    """funcao que substitue os caracteres por espacos
    str -> str"""
    for caracteres in "_,:;,.~^*&"%$@?!"
        frase = frase.replace(caracteres," ")
    return frase