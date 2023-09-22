def retira_pontuacao(frase):
    ''' funcao que retira a pontuacao da frase e a subsititui por espacos; string->string'''
    lista=[]
    lista[:]=frase
        if','in lista:
            lista[list.index(lista,','):list.index(lista,',')]=' '
        if '.' in lista:
            lista[list.index(lista,'.'):list.index(lista,'.')]=' '
        if '!' in lista:
            lista[list.index(lista,'!'):list.index(lista,'!')]=' '
        if '?' in lista:
            lista[list.index(lista,'?'):list.index(lista,'?')]=' '
        if '...' in lista:
            lista[list.index(lista,'...'):list.index(lista,'...')]=' '
        if ':' in lista:
            lista[list.index(lista,':'):list.index(lista,':')]=' '
        if ';' in lista:
            lista[list.index(lista,';'):list.index(lista,';')]=' '
        if '-' in lista:
            lista[list.index(lista,'-'):list.index(lista,'-')]=' '
    return str(lista)