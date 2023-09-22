def retira_pontuacao(string):
    '''funcao dada uma frase retorna a mesma sem nenhuma pontuacao'''
    str.replace(string, '.', ' ')
    str.replace(string, '-', ' ')
    str.replace(string, ',', ' ')
    str.replace(string, ':', ' ')
    str.replace(string, ';', ' ')
    return string