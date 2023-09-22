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

def invert(frase):
    '''funcao que inverte a frase sem pontuacao e letra maiuscula str->str'''
    frase1=retira_pontuacao(frase)
    frase2=frase1.lower()
    frase3=frase2.split()
    frase4=frase3[::-1]
    frase5=' '.join(frase4)
    return frase5