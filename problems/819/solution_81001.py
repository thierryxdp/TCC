def filtraMultiplos(lista,n):
	"""filtra os multiplos de um numero n
int,int->"""
ListaA = []
Variavel = 0
while variavel < len(lista):
    if lista[variavel] %n ==0:
        list.append(ListaA,lista[variavel])
        variavel = variavel+1
        return ListaA