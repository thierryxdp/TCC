def retira_pontuacao(string):
    pontuacao = ["!", "?", "...", ".", "-", ",", ":", ";"]
    string = string.replace('!', ' ')
    string = string.replace('?', ' ')
    string = string.replace('...', ' ')
    string = string.replace('.', ' ')
    string = string.replace('-', ' ')
    string = string.replace(',', ' ')
    string = string.replace(':', ' ')
    string = string.replace(';', ' ')
    no_punct = ""
    for char in string:
       if char not in pontuacao:
           no_punct = no_punct + char
    return no_punct