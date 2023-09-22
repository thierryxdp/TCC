def retira_pontuacao (frase):
    '''Função que, dado uma frase, remove a pontuação e a substitui
    por espaços
    str -> str'''
    
    if virgula and travessao and ponto in frase:
        return frase.replace(' ')