def retira_pontuacao(f):
    '''
    A função retorna uma frase onde todos os 
    tipos de pontuação são substituidos por sepaço
    (entrada = str / saída = str)
    '''
    s = str.replace(f, '...', '[]')
    return str.replace(s, '.?![]:;,-', ' ')