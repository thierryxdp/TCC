retira_pontuacao (frase):
    """funcao que retira os caracteres e substitue todos por espaco de uma determinada frase dada
    str -> str"""
    for caracteres in "-,:;,.~^*&%":
        frase = frase.replace(caracteres,"")
        return frase