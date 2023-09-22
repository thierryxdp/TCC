def retira_pontuacao(frase):
    frasef = str.replace(str.rstrip(frase,'!'),'.', ' ')
    return frasef