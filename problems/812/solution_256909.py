def retira_pontuacao(string):
    string = string.replace('!', ' ')
    string = string.replace('?', ' ')
    string = string.replace('...', ' ')
    string = string.replace('.', ' ')
    string = string.replace('-', ' ')
    string = string.replace(',', ' ')
    string = string.replace(':', ' ')
    string = string.replace(';', ' ')
    return string