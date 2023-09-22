'''Função que recebe uma lista de inteiros e um inteiro e retorna uma nova lista
com os inteiros da lista inicial maiore que o inteiro dado'''
'''list(int),int --> list(int) '''
def maiores(lista,n):
    x=[]
    z=-1
    teste = -1
    aux = -1
    for y in lista:
        z+=1
        if n < lista[z]:
        	x.append(y)
	x.sort()
    return x