def retira(frase):

    pontuacao = '!' or ',' or '.' or ';' or '?' or ':'

    if pontuacao in frase:
        return str.replace(frase,pontuacao,' ')