def retira_pontuacao(frase):
    '''
    
    '''
    tipos_pontuacoes = ['-', ',', ':', ';', '.', '!', '?']
   	pontuacao = str in tipos_pontuacoes
    
    return str.replace((frase), 'pontuacao', ' ')