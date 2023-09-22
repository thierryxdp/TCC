def retira_pontuacao(frase):
    
    travessao = frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    doispontos = virgula.replace(':', ' ')
    pontovirgula = doispontos.replace(';', ' ')
    pontofinal = pontovirgula.replace('.', ' ')
    pontointerrogacao = pontofinal.replace('?', ' ')
    ponto_exclamacao = pontointerrogacao.replace('!', ' ')
    return ponto_exclamacao



def inverte(frase):
    """Dada uma frase esta função retornará a frase invertida e sem pontuação.
    str -> str
    str -> str"""
    removePontos = retira_pontuacao(frase)
    fraseMinuscula = removePontos.lower()
    removeEspacos = fraseMinuscula.strip()
    novaFraseSplit = removeEspacos.split()[::-1]
    novaFraseJoin = " ".join(novaFraseSplit)
    return novaFraseJoin