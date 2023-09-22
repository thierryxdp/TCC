def retira_pontuacao (frase):
    '''Função que, dado uma frase, remove a pontuação e a substitui
    por espaços
    str -> str'''
    pontuacao = ',', '-', '.', ':', ';', '?', '!'
    
    if pontuacao in frase:
        return frase.replace(pontuacao, ' ')