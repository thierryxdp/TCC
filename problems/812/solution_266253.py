def retira_pontuacao (frase):
    '''Função que retira a pontuação de uma frase
    string -> string'''
    
    novo = []
for x in lista:
    item = x
    for y in ['\n', '\t', '/', '.', '-', '(', ')']:
        item = item.replace(y, "")
    novo.append(item)