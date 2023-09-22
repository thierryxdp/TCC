def retira_pontuacao(frase):
    '''rertira todas as pontuacoes de uma frase e substtituii por espacco'''
    travessao= frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    doispontos = virgula.replace(':', ' ')
    pontovirgula = doispontos.replace(';', ' ')
    pontofinal = pontovirgula.replace('.', ' ')
    pontointerrogacao = pontofinal.replace('?', ' ')
    pontoexclamacao = pontointerrogacao.replace('!', ' ')
    
    return pontoexclamacao