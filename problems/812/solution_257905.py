def retira_pontuacao (frase):
    '''Retorna a frase com caracteres de pontuação substituídos por espaço
    string-> string'''
    n1 = frase.replace('_',' ',)
    n2 = n1.replace(',',' ',)
    n3 = n2.replace(':',' ',)
    n4 = n3.replace('-',' ',)
    if n4[-3:] == '...':
        return n4[:-3] + ' '
    else:
        return n4[:-1] + ' '