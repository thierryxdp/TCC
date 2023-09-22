def retira_pontuacao(string):
    '''funcao dada uma frase retorna a mesma sem nenhuma pontuacao'''
    a = string.replace('.', ' ') and string.replace('-', ' ') and string.replace(',', ' ') and string.replace(':', ' ') and string.replace(';', ' ')
    return a