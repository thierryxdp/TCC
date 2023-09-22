def retira_pontuacao(frase):
    travessao= frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    doispontos = virgula.replace(':', ' ')
    pontovirgula = doispontos.replace(';', ' ')
    pontofinal = pontovirgula.replace('.', ' ')
    pontointerrogacao = pontofinal.replace('?', ' ')
    pontoexclamacao = pontointerrogacao.replace('!', ' ')
    
    return pontoexclamacao