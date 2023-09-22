def retira_pontuacao(frase):
    'retira todos os caracteres de pontuacao de uma frase str->str'
    return str.replace(frase, '.' or ',' or ':' or'-', ' ')