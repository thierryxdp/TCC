#Start your python function here
def eh_par(num):
    '''retorna True se um numero é par ou False se é impar. int/float ->bool'''
    return num%2==0
def filtra_pares(lista):
    resultado=()
	if eh_par(lista(0)):
    	resultado+=lista[0:1]
	if eh_par(lista(1)): 
   		resultado+=lista(1:2)
	if eh_par(lista(2)):
		resultado+=lista(2:3)
	if eh_par(lista(3)):
    	resultado+=lista(3:)
    return resultado