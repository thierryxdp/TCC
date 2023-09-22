def faltante(n):
    '''A funcao recebe uma lista com a enumeracao de pecas e retorna qual das pecas esta faltando
list->int'''
    n.sort()
    n.append(' ')
    lista=list(range(1,len(n)+2))
    ordem=0
    falta=[]
    while ordem<len(n):
        if n[ordem]!=lista[ordem]:
            return lista[ordem]
        if n[ordem] in lista:
            ordem=ordem+1