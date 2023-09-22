def retira_pontuacao(frase):
    """
    	Recebe uma frase e retorna uma nova frase em que suas
        pontuações foram substituidas por espaços.
        str --> str
    """
    
    ponto = str.replace(frase, '.', ' ')
    interrogacao = str.replace(ponto, '?', ' ')
    exclamacao = str.replace(interrogacao, '!', ' ')
    travecao = str.replace(exclamacao, '-', ' ')
    virgula = str.replace(travecao, ',', ' ')
    doisPontos = str.replace(virgula, ':', ' ')
    pontoVirgula = str.replace(doisPontos, ';', ' ')
    fraseFinal = pontoVirgula[:]
    return fraseFinal

def inverte(frase):
    fraseSemPontuacao = retira_pontuacao(frase)
    frasePartida = str.split(fraseSemPontuacao, ' ')
    tamDaFrase = len(frasePartida)
    indice = 0
    while indice<tamDaFrase:
    	fraseInvertida = list.push(frasePartida[-indice])
        indice = indice + 1 
    return fraseInvertida