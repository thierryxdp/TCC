def retira_pontuacao(frase):
    '''
    
    '''
    tipos_pontuacoes = ['-', ',', ':', ';', '.', '!', '?']
    if pontuacao in tipos_pontuacoes:
        return str.replace((frase), pontuacao, ' ')