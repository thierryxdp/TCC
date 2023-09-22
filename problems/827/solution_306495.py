def qtd_divisores(num):
    " " "Conta a quantidades de divisores um número tem; int, -> int" " "
	valores = []
	for i in list(range(1,num+1)):
    	valores.append(i)
	resultado = len(filter(lambda x: x%num==0,valores)))               
	return resultado