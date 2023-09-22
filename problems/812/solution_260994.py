def retira_pontuacao(frase):
    if (',' or '-' or '.' or ':' or ';') in frase:
        return frase.replace((',','-','.',':',';'),' ')