def retira_pontuacao (frase):
    '''Retorna a frase com caracteres de pontuação substituídos por espaço
    string-> string'''
    n1 = frase.replace('_','',)
    n2 = n1.replace(',','',)
    n3 = n2.replace(':','',)
    if n2[-3:] == '...':
        return n2[:-3]
    else:
        n2[:-1]