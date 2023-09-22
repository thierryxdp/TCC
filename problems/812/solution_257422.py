def retira_pontuacao(frase):
    texto1 = frase.replace('!',' ')
    texto2 = texto1.replace('.',' ')
    texto3 = texto2.replace(',',' ')
    texto4 = texto3.replace('-',' ')
    texto5 = texto4.replace(':',' ')
    texto6 = texto5.replace(';',' ')
    return texto6