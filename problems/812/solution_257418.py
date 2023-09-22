def retira_pontuacao(frase):
    texto1 = frase.replace('!',' ')
    texto2 = frase.replace('.',' ')
    texto3 = frase.replace(',',' ')
    texto4 = frase.replace('-',' ')
    texto5 = frase.replace(':',' ')
    texto6 = frase.replace(';',' ')
    final = [texto1,texto2,texto3,texto4,texto5,texto6]
    return final