def retira_pontuacao(frase):
    '''Função que retorna uma frase sem pontuação das informação 'frase' de entrada: str ->str'''
    remove1 = str.replace(frase, '-', ' ')
    remove2 = str.replace(remove1, '.', ' ')
    remove3 = str.replace(remove2, '?', ' ')
    remove4 = str.replace(remove3, '!', ' ')
    remove5 = str.replace(remove4, ',', ' ')
    remove6 = str.replace(remove5, ':', ' ')
    remove7 = str.replace(remove6, ';', ' ')

    return remove7