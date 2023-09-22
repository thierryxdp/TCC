def retira_pontuacao(frase):
    """Dada uma frase pontuada, remove todos os pontos como travessão, vírgula, dois pontos, ponto e vírgula
    e ponto final substituindo por espaço.
     str -> str"""
    travessao = frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    doispontos = virgula.replace(':', ' ')
    pontovirgula = doispontos.replace(';', ' ')
    pontofinal = pontoVirgula.replace('.', ' ')
    pontointerrogacao = pontofinal.replace('?', ' ')
    pontoExclamacao = pontoniterrogacao.replace('!', ' ')
    return pontoExclamacao