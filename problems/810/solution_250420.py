def retira_pontuacao(frase1):
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase, '-', ' '), ',', ' '), ';', ' '), ':', ' '), '!', ' '), '?', ' '), '.', ' '), '...', ' ')
def inverte(frase):
    str.join(list.reverse(str.split(retira_pontuacao(frase))))