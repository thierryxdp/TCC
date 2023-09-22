def retira_pontuacao(f):
    '''
    Recebe uma frase em uma string e vai substituindo todos os 
    possíveis casos de pontuação por um espaço simples.
    str -> str
    '''
    
    f = f.replace('-', ' ')
    f = f.replace(',', ' ')
    f = f.replace(':', ' ')
    f = f.replace(';', ' ')
    f = f.replace('!', ' ')
    f = f.replace('?', ' ')
    f = f.replace('.', ' ')
    
    return f