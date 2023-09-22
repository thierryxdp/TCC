def retira_pontuacao(frase1):
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase1, '-', ' '), ',', ' '), ';', ' '), ':', ' '), '!', ' '), '?', ' '), '.', ' '), '...', ' ')
def inverte(frase):
    return str.join(list.reverse(str.split(retira_pontuacao(frase))),' ')