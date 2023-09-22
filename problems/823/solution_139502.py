def faltante(pecas):
	'''função recebe uma lista
    com as peças e retorna quais estão faltando'''
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