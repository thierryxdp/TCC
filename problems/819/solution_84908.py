#Função que recebe uma lista(numeros) e um numero(n) e retorna uma lista com os
#numeros que são multiplos de (n)
#list, int -> list
def filtraMultiplos(numeros, n):
	listaNum = []
    i = 0
    while i < len(numeros):
        if numeros[i]%n == 0:
        	listaNum.append(numeros[i])
    	i+=1
    return listaNum