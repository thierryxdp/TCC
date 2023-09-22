def retira_pontuacao(frase):
    '''Função que dada uma frase, retorna a mesma frase substituindo os caracteres de pontuação por espaço.  ent-> string  saida-> string'''
    
    
    lista = frase.split('_')
    lista = frase.split(',')
    lista = frase.split(':')
    lista = frase.split(';')
    lista = frase.split('.')
    lista = frase.split('!')
    lista = frase.split('?')
    lista = frase.split('...')
    
    return frase