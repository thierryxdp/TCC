def retira_pontuacao(frase):
    """Dada uma string (frase), a função retorna a frase onde todos os carcateres de pontuação
    tenham sido substituídos por espaço
    str -> str"""
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase, "-", " "), ",", " "), ":", " "), ";", " "), ".", " "), "!", " "), "?", " "), "...", " ")