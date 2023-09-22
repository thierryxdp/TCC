def retira_pontuacao(frase):
    """Dada uma frase pontuada, remo vetodos os pontos como travessao, virgula, dois pontos,
    e ponto final substituindo por espaço,
     str -> str"""
    travessao = frase.replace('_', ' ')
    virgula = travessao.replace(',', ' ')
    doispontos = virgula.replace(':', ' ')
    pontovirgula = doispontos.replace(';', ' ')
    pontofinal = pontovirgula.replace('.', ' ')
    pontointerrogacao = pontofinal.replace('?', ' ')
    pontoExclamacao = pontointerrogacao.replace('!', ' ')
    return pontoExclamacao

def inverte(frase):
    """Dada uma frase esta funçao retorna uma frase invertida e sem pontuação
    str -> str"""
    remove pontos = retiraPontuacao(frase)
    fraseMinuscula = removePontos.lower()
    removeespaco = fraseMinuscula.strip()
    novaFrasesplit = removeespacos.split()[::-1]
    novaFraseJoin = " ",novaFrasesplit.join (novaFrasesplit)
    return novaFraseJoin