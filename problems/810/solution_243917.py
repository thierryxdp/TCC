def retira_pontuacao(frase):
    """
    Dada uma frase pontuada, remove todos os pontos como travessão, vírgula, dois pontos, ponto e vírgula
    e ponto final transformando-os em um espaço.
    
    str -> str
    """
    
    travessao = frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    doisPontos = virgula.replace(':', ' ')
    pontoVirgula = doisPontos.replace(';', ' ')
    pontoFinal = pontoVirgula.replace('.', ' ')
    pontoInterrogacao = pontoFinal.replace('?', ' ')
    pontoExclamacao = pontoInterrogacao.replace('!', ' ')
    return pontoExclamacao



def inverte(frase):
    """
    Dada uma frase esta função retornará a frase invertida e sem pontuações.
    
    str -> str
    """
    removePontos = retira_pontuacao(frase)
    fraseMinuscula = removePontos.lower()
    removerEspacos = fraseMinuscula.strip()
    novaFraseS = removerEspacos.split()[::-1]
    novaFraseJ = " ".join(novaFraseS)
    return novaFraseJ