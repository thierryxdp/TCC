'''Função que recebe uma lista de números e um número e retorna uma nova lista de 
números com todos os elementos da lista inicial que são divisíveis pelo número dado'''
'''list(floats),float --> list(floats)'''
def filtraMultiplos(lista,n):
    y=[]
	for x in lista:
        if x%n==0:
            y.append(x)
    return y