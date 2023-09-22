def filtra(x,num):
    return x % num == 0

def qtd_divisores(num):
    " " "Conta a quantidades de divisores um número tem; int, -> int" " "
	valores = []
	for i in list(range(1, num+1)):
    	valores.append(i)
	resultado = len(list(filter(filtra,valores,num)))               
	return resultado