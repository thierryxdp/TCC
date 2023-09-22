def inverte(frase):
    """Retorna uma frase na ordem inversa, sem pontuação
    ou letras maiúsculas;
    str -> str"""
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    frase = str.split(frase)
    list.reverse(frase)
    frase_inversa = str.join(" ",frase)
    return frase_inversa