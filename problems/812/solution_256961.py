import re
def retira_pontuacao(frase):
    'função que dado uma frase a retorna com espaço no lugar da pontuação'
    pontucao = re.sub(r'[^\w\s]', '', s)
    return pontuacao