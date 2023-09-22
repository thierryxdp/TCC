def retira_pontuacao(frase):
    """Função que dada uma frase, substitui os caracteres de pontuação por espaço;
    str -> str"""
    if "!"+"?":
        return str.replace(frase,"!"," ")