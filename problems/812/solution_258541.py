def retira_pontuacao(pontos):
    '''retorna a frase onde os caracteres de pontuacao
    sao substituidos por espaco'''
    return str.replace(pontos, '.','!','?', '...',' ')