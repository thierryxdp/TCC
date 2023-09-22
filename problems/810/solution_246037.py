def retira_pontuacao(s):
    new_string = s
    to_remove=["-",":",";",".","?","!"]
    for x in to_remove:
        new_string = new_string.replace(x, ' ')
    return new_string

def inverte(s):
    lista = retira_pontuacao(s)
    lista1 = lista.split()
    invertida = lista1.reverse()
    invertida_str = ','.join(invertida)
    return retira_pontuacao(invertida_str)