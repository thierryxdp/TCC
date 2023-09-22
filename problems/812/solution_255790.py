def retira_pontuacao(x):
    """Dada uma frase retorna ela com os caracteres de pontuação substituídos por espaço""" 
    x = x.replace('.', ' ')
    x = x.replace(',', ' ')
    x = x.replace(':', ' ')
    x = x.replace(';', ' ')
    x = x.replace('!', ' ')
    x = x.replace('?', ' ')
    x = x.replace('-', ' ')
    x = x.replace('"', ' ')
    return x