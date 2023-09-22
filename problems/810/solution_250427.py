def retira_pontuacao(frase1):
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase1, '-', ' '), ',', ' '), ';', ' '), ':', ' '), '!', ' '), '?', ' '), '.', ' '), '...', ' ')
def inverte(frase):
    reverte = list.reverse(str.split(retira_pontuacao(frase)))
    return str.join(' ', reverte)