def retira_pontuacao(frase):
    '''essa funçao retorna uma frase com todas as suas pontuaçoes substituidas por espaço
    str -> str'''

    return frase.replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('...',' ').replace('.',' ').replace('!',' ').replace('?',' ')


def inverte(frase):
    '''essa funçao retorna, a partir de uma frase, uma segunda frase, com ordem contraria e sem pontuaçao.
    str-> str'''
    frase1= str.lower(frase)
    frase2= frase1 retira_pontuacao
    frase3= str.split(frase2)[: : -1]
    
    return str.join(' ', frase3)