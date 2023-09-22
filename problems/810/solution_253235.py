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
    contador = 0
    while contador < len(fraseRepartida):
    	if contador == 0 or contador == len(fraseRepartida):
            palavraInvertida += fraseRepartida[contador]
        else:
            palavraInvertida += " " +fraseRepartida[contador]
        contador += 1
    return palavraInvertida