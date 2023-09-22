import string
def retira_pontuacao(frase):
    'função que dado uma frase a retorna com espaço no lugar da pontuação'
    saida = frase.translate(string.maketrans(' ', ' '), string.punctuation)
    return saida