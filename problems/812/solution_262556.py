def retira_pontuacao(frase):
    """Funçao que Dada uma frase pontuada, remove a travessão, vírgula, dois pontos, ponto e vírgula
    e ponto final transformando-os em um espaço.
    str->"""
    travessao = frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    doisPontos = virgula.replace(':', ' ')
    pontoVirgula = doisPontos.replace(';', ' ')
    pontoFinal = pontoVirgula.replace('.', ' ')
    pontoInterrogacao = pontoFinal.replace('?', ' ')
    pontoExclamacao = pontoInterrogacao.replace('!', ' ')
    return pontoExclamacao