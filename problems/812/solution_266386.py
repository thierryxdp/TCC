def retira_pontuacao(string):
    '''funcao dada uma frase retorna a mesma sem nenhuma pontuacao'''
    string.replace('.', ' ')
    string.replace('-', ' ')
    string.replace(',', ' ')
    string.replace(':', ' ')
    string.replace(';', ' ')
    return string