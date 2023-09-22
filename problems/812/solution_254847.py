def retira_pontuacao(texto):
    texto1 = texto.replace('.', ' ')
    texto2 = texto1.replace('!', ' ')
    texto3 = texto2.replace('?', ' ')
    texto4 = texto3.replace('-', ' ')
    texto5 = texto4.replace(',', ' ')
    texto6 = texto5.replace(':', ' ')
    texto7 = texto6.replace(';', ' ')
    return novo_texto