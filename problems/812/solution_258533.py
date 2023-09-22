def retira_pontuacao(pontos):
    '''retorna a frase onde os caracteres de pontuacao
    sejam substituidos por espaco'''
    return str.replace(pontos,'.','!','?','...',' ')