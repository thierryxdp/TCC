def retira_pontuacao(s):
    new_string = s
    to_remove=["-",",",":",";",".","?","!"]
    for x in to_remove:
        new_string = new_string.replace(x, ' ')
    return new_string

def inverte(s):
    return sorted.reversed(retira_pontuacao(s))