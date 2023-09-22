def retira_pontuacao(frase):
    '''---'''
    remove1 = str.replace(frase, '-', ' ')
    remove2 = str.replace(remove1, '.', ' ')
    remove3 = str.replace(remove2, '?', ' ')
    remove4 = str.replace(remove3, '!', ' ')
    remove5 = str.replace(remove4, ',', ' ')
    remove6 = str.replace(remove5, ':', ' ')
    remove7 = str.replace(remove6, ';', ' ')

    inversa = remove7[::-1]
    return inversa