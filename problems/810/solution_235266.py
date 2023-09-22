def inverte (frase):
    '''
    A função retorna uma frase
    invertida e sem pontuação.
    string -> string
    '''
    lista = str.split(retira_pontuacao(frase)," ")
    list.reverse(lista)
    return srt.join(" ",lista)