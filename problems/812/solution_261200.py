def retira_pontuacao(frase):
    nova_frase = str.replace(frase,frase[-1],' ')
    nova_frase1 = str.replace(frase,',',' ')
    return nova_frase