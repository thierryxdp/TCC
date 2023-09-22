def retira_pontuacao (frase):
    '''Função que retira a pontuação de uma frase
    string -> string'''
    
    for y in ['\n', '\t', '/', '.', '-', '(', ')']:
        item = item.replace(y, "")
    frase.append(item)