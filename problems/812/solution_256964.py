def retira_pontuacao(frase):
    'função que dado uma frase a retorna com espaço no lugar da pontuação'
    pontuacao = frase.replace('!', ' ') or frase.replace('?', ' ')
    return pontuacao