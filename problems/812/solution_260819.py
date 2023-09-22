def retira_pontuacao(texto):
    '''Funcao recebe uma uma frase e retrona uma frase substituindo sua pontuacao por ' '
string -> string'''
    subreticen = str.join(" ", str.split(texto, '...'))
    subPonto = str.join(" ", str.split(subreticen, '.'))
    subvirgula = str.join(" ", str.split(subPonto, ','))
    subPontoVirgula = str.join(" ", str.split(subvirgula, ';'))
    subDoispontos = str.join(" ", str.split(subPontoVirgula, ':'))
    subTrave = str.join(" ", str.split(subDoispontos, '-'))
    subdEsclama = str.join(" ", str.split(subTrave, '!'))
    subInterrogacao = str.join(" ", str.split(subdEsclama, '?'))
    return subInterrogacao