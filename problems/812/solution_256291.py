def retira_pontuacao(frase):
    return str.replace(str.replace(str.replace(frase,'!',' '), '?',' '),'.',' ')