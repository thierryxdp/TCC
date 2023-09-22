def retira_pontuacao(frase):
    '''essa funçao retorna uma frase com todas as suas pontuaçoes substituidas por espaço
    str -> str'''
    return frase.replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('...',' ').replace('.',' ').replace('!',' ').replace('?',' ')