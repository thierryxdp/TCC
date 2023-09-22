def retira_pontuacao(frase):
    pontuacao = ['!','.','?',';',':','-']
    nova_frase = str.replace(frase,pontuacao,' ')
    return nova_frase