def retira_pontuacao (frase):
    '''Retorna a frase dada na entrada, em string, porém
    sem a pontuação
    str --> str'''
    travessao = str.replace(frase, '-', ' ')
    ponto = str.replace(travessao, '.', ' ')
    exclamacao = str.replace(ponto, '!', ' ')
    interrogacao = str.replace(exclamacao, '?', ' ')
    pontovirgula = str.replace(interrogacao, ';', ' ')
    virgula = str.replace(pontovirgula, ',', ' ')
    doispontos = str.replace(virgula, ':', ' ')
    
    return doispontos

def inverte (frase):
    '''Retorna a ordem inversa da frase, em string,
    dada como parâmetro, com todas as letras minúsculas
    e sem pontuação
    str --> str'''
    pontuacao = retira_pontuacao (frase)
    lista = str.split(pontuacao)
    list.reverse(lista)
    inversa = str.join(' ', lista)
    minuscula = str.lower(inversa)
    return minuscula