def retira_pontuacao(frase):
    '''Verifica e retorna a frase substituindo a pontuação por espaço;
    str->str'''
    pontuacao = ['.', ';', ':', '?', '!', '-', ',','...']
    for i in range(len(pontuacao)):
        frase = frase.replace(pontuacao[i], " ")
    return frase