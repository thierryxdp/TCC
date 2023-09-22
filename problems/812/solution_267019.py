def retira_pontuacao(frase):
    ''' funcao que retira a pontuacao da frase e a subsititui por espacos; string->string'''
    lista[:]=frase
    rem=[',','.','!','...',':',';','-','?']
    list.remove (lista,rem)
    return str(lista)