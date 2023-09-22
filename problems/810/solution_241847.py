def inverte(frase):
    '''função que retorna o inverso da frase inicial sem maiúsculas e sem pontuação, string -> string'''
    frase_sem_pont_min=retira_pontuacao(frase).lower()
    lista=frase_sem_pont_min.split()
    lista_invertida=lista.reverse()
    return (' '.join(lista))