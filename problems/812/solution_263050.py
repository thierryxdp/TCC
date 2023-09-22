def retira_pontuacao(frase):
    """Recebe uma frase, substitui caracteres de pontuacao substituidos por espaco e retorna a frase; str-> str."""
    str.replace(frase,"..."," ")
    str.replace(frase,"."," ")
    str.replace(frase,"!"," ")
    str.replace(frase,"?", " ")
    str.replace(frase, "-", " ")
    str.replace(frase,","," ")
    str.replace(frase,":"," ")
    str.replace(frase,";"," ")
    return frase