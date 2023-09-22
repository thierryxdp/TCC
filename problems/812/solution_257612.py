def retira_pontuacao(frase):
    frase1 = str.replace(frase, '.',' ')
    if frase == '.':
        return frase1