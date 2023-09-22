def retira_pontuacao(frase):
    '''descricao '''
    virgula = str.replace(frase,",","@")
    return str.strip(frase, '/.@:!?')