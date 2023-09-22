def retira_pontuacao(frase):
    return frase.translate(frase.maketrans({'.': ' ', '?': ' ', '!': ' ', ',': ' ', '-': ' ', ':': ' ', ':': ' ', ';': ' ', '...': ' '}))