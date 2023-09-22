def retira_pontuacao(frase):
    '''Substitui a pontuação da frase por espaços vazios e retorna
    uma frase sem nenhuma pontuação.'''
    f = frase.split('_')
    frase = ' '.join(f)
   
    f = frase.split(',')
    frase = ' '.join(f)
   
    f = frase.split(':')
    frase = ' '.join(f)
   
    f = frase.split(';')
    frase = ' '.join(f)
   
    f = frase.split('.')
    frase = ' '.join(f)
   
    return frase