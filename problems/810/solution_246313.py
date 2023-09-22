def retira_pontuacao(s):
    new_string = s
    to_remove=["-",":",";",".","?","!",","]
    for x in to_remove:
        new_string = new_string.replace(x, ' ')
    return new_string

def retira_pontuacao1(s):
    new_string = s
    to_remove=[","]
    for x in to_remove:
        new_string = new_string.replace(x, ' ')
    return new_string

def inverte(s):
    lista = retira_pontuacao(s)
    lista1 = lista.split()
    lista1.reverse()
    invertida_str = ','.join(lista1)
    invertida_M = retira_pontuacao1(invertida_str)
    return str.lower(invertida_M)