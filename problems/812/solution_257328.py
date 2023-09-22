def retira_pontuação(frase):
    ''' Retira todos os caracteres de pontuação da frase.
    '''
    lista = list(frase)
    antes = len(lista)
    lista2 = list.remove(lista, ',')