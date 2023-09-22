def qtd_divisores(num):
    cont = 0
    for n in range(1,num+1):
       	if num % n==0:
        	cont += 1
       		return cont