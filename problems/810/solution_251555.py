def retira_pontuacao (texto):
    """ Substiu a pontuação da frase por espaço. Str -> str"""
    t1 = str.replace(texto,'-', ' ')
    t2 = str.replace(t1, '...', ' ')
    t3 = str.replace(t2, '.', ' ')
    t4 = str.replace(t3, ':', ' ')
    t5 = str.replace(t4, ',', ' ')
    t6 = str.replace(t5, ';', ' ')
    t7 = str.replace(t6, '!', ' ')
    t8 = str.replace(t7, '?', ' ')
    return t8
def inverte (frase):
    """Retorna a frase com as palavras na ordem inversa, sem pontuação e sem pontuação. str -> lista"""
    fr = (retira_pontuacao(frase))
    fr2 = str.lower(fr)
    listafrase = str.split(fr2)
    listafat = listafrase[::-1]
    final= str.join(" ", listafat)
    return final