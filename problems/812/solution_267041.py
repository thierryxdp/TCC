def retira_pontuacao(frase):
    ''' funcao que retira a pontuacao da frase e a subsititui por espacos; string->string'''
    lista=[]
    lista[:]=frase
    while ',' in lista:
        if ',' in lista:
            lista[list.index(lista,',')]=' '         
    while '.'in lista:
            if '.' in lista:
                lista[list.index(lista,'.')]=' '
    while '!'in lista:
            if '!' in lista:
                lista[list.index(lista,'!')]=' '
    while '?'in lista:
            if '?' in lista:
                lista[list.index(lista,'?')]=' '
    while '...'in lista:
            if '...' in lista:
                lista[list.index(lista,'...')]=' '
    while ':' in lista:
            if ':' in lista:
                lista[list.index(lista,':')]=' '
    while ';' in lista:
            if ';' in lista:
                lista[list.index(lista,';')]=' '
    while '-' in lista:
            if'-' in lista:
                lista[list.index(lista,'-')]=' '
    
    result=''.join(lista)
    return result