def retira_pontuacao(texto):
    '''Essa função retorna um texto com as ponntuações retiradas'''
    for x in '.:;-,':
        texto=texto.replace(x,' ')
    return texto