def qtd_divisores(num):
    '''retorna quantos divisores o número de entrada tem; int -> int'''
    divisores=0
    if num<0:
        return 0
    anteriores=list(range(num))+[num]
    anteriores.remove(0)
    for i in anteriores:
        if num%i==0:
            divisores=divisores+1
	return divisores