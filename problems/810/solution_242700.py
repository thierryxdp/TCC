def substitui(texto):
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


def inverte(frase):
    '''Funcao recebe uma frase e retorna a mesma frase, porem, ivertida, sem nenhuma pontuacao e com letras minusculas
string - > string'''
    removPonto = substitui(frase)
    return str.lower(str.join(' ',str.split(removPonto)[-1::-1]))