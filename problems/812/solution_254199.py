def retira_pontuação(frase):
    if C[len(C) - 1] == '!':
        return str.replace(frase,"!", "")