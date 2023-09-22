def retira_pontuacao(frase):
    'função que dado uma frase a retorna com espaço no lugar da pontuação'
    pontuacao = retira_pontuacao.translate(str.maketrans('', '', string.punctuation))
    return pontuacao