def retira_pontuacao(string):
    '''funcao dada uma frase retorna a mesma sem nenhuma pontuacao'''
    a = str.replace(string, ',', ' ')
    b = str.replace(a, '.', ' ')
    c = str.replace(b, '-', ' ')
    d = str.replace(c, ':', ' ')
    e = str.replace(d, ';', ' ')
    return e