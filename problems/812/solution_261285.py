def retira_pontuacao(f):
    '''
    A fução retorna uma frase onde todas as pontuações
    são substituidas por espaços
    (entrada = str / saída = str)
    '''
    f = str.replace(f, '...', '[]')
    f = str.replace(f, '[]', ' ')
    f = str.replace(f, '.', ' ')
    f = str.replace(f, ',', ' ')
    f = str.replace(f, ';', ' ')
    f = str.replace(f, ':', ' ')
    f = str.replace(f, '-', ' ')
    f = str.replace(f, '!, ' ')
    f = str.replace(f, '?', ' ')
    return f