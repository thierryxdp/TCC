def retira_pontuacao(frase):
    """
    	Recebe uma frase e retorna uma nova frase em que suas
        pontuações foram substituidas por espaços.
        str --> str
    """
    
    ponto = str.replace(frase, '.', ' ')
    interrogacao = str.replace(ponto, '?', ' ')
    exclamacao = str.replace(interrogacao, '!', ' ')
    travessao = str.replace(exclamacao, '-', ' ')
    virgula = str.replace(travessao, ',', ' ')
    doisPontos = str.replace(virgula, ':', ' ')
    pontoVirgula = str.replace(doisPontos, ';', ' ')
    return pontoVirgula

def inverte(frase):
    fraseSemPontuacao = retira_pontuacao(str.lower(frase))
    fraseRepartida = str.split(fraseSemPontuacao)
    list.reverse(fraseRepartida)
    palavraInvertida = ''
    for palavra in fraseRepartida:
        palavraInvertida += palavra + " "
    return palavraInvertida