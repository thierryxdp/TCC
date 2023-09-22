def retira_pontuacao(frase1):
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase1, '-', ' '), ',', ' '), ';', ' '), ':', ' '), '!', ' '), '?', ' '), '.', ' '), '...', ' ')
def inverte(frase):
    divide = str.split(retira_pontuacao(frase))
    reverte = list.reverse(divide)
    return str.join(' ', reverte)