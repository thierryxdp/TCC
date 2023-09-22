def retira_pontuacao(frase):
    'função que dado uma frase a retorna com espaço no lugar da pontuação'
    pontuacao = [',', '.', ';', ':', '/', '!', '?']
    espaco = frase.replace(pontuacao, ' ')
    return espaco