def retira_pontuacao(frase):
    '''Retira a pontuação da frase de entrada, 
       substituindo-as por espaços em branco;
       str -> str'''
    return frase.replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace(frase[-1],' ')
#
def inverte(frase):
    '''Inverte a frase de entrada, retornando-a também
       sem letras maiúsculas e sem pontuação;
       str -> str'''
    listaFrase=retira_pontuacao(frase).lower().split(' ')
    while '' in listaFrase:
        listaFrase.remove('')
    return str.join(' ',listaFrase[::-1])