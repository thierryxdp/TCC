def retira_pontuacao(frase):
    """Função que dada uma frase retira todos os caracteres de pontuação e os substitui por espaço
    str -> str"""
    return str.replace(str.replace(str.replace(str.replace(str.replace(frase, '.', ' ')), ';', ' '), ':', ' '), ',', ' '), '-', ' ')