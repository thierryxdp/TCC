def retira_pontuacao(frase):
    '''Função que dada uma frase, retorna a mesma frase substituindo os caracteres de pontuação por espaço.  ent-> string  saida-> string'''
    
    frase = frase.split('_')
    frase = frase.split(',')
    frase = frase.split(':')
    frase = frase.split(';')
    frase = frase.split('.')
    frase = frase.split('!')
    frase = frase.split('?')
    frase = frase.split('...')