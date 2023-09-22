def retira_pontuacao(frase):
    texto1 = [frase.replace('!',' '),frase.replace('.',' '),frase.replace(',',' '),frase.replace('-',' '),frase.replace(':',' '),frase.replace(';',' ')]
    texto2 = frase.replace('.',' ')
    texto3 = frase.replace(',',' ')
    texto4 = frase.replace('-',' ')
    texto5 = frase.replace(':',' ')
    texto6 = frase.replace(';',' ')
    return texto1