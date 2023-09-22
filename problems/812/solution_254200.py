def retira_pontuação(frase):
    if frase[len(frase) - 1] == '!':
        return str.replace(frase,"!", "")