# Dado um número inteiro n, esta função retorna a quantidade de divisores de n.
# Notemos que caso n seja não positivo, a função retorna 0, por definição de
# divisor.
# int -> int

from math import ceil
def qtd_divisores(n):
    
    if n<=0: #Caso: número não positivo
        cont =0
    else: #Caso: números inteiros positivos
    	cont =1 #Considerando que n é divisor de n
    
    	for i in range(1, ceil(n/2)+1): # buscando os demais divisores, caso existam
        	if n%i ==0:
            	cont += 1
            
    return cont