def retira_pontuacao(frase):
    'retira todos os caracteres de pontuacao de uma frase str->str'
    return str.replace(frase, '.' not ',' or ':' or '-', ' ')