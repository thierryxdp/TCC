def retira_pontuacao(f):
    '''
    A fução retorna uma frase onde todas as pontuações
    são substituidas por espaços
    (entrada = str / saída = str)
    '''
    s = str.replace(f, '...', '[]')
    s = str.replace(f, '[]', ' ')
    s = str.replace(f, '.', ' ')
    s = str.replace(f, ',', ' ')
    s = str.replace(f, ';', ' ')
    s = str.replace(f, ':', ' ')
    return s