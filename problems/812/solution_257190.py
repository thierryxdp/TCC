def retira_pontuacao(old):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string