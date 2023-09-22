def faltante(pecas):
	pecas.sort()
    pecas.append('')
    lista=list(range(1,len(pecas)+2))
    ordem=0
    falta=[]
    while ordem<len(pecas):
        if pecas[ordem]!=lista[ordem]:
            return lista[ordem]
        if pecas[ordem] in lista:
            ordem=ordem+1