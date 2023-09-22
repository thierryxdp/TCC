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