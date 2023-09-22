def filtraMultiplos(lista,n):
	''' filtra os multiplos do numero n presentes na lista informada, retornando uma nova lista somente com os multiplos
    list,int -> list'''
    posicao = 0
    nova_lista = []
    while posicao < len(lista):
    	if lista[posicao]%n==0:
        	nova_lista = nova_lista + [lista[posicao],]
        posicao = posicao + 1
    return nova_lista