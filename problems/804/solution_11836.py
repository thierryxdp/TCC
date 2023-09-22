def filtra_pares(numeros):
    '''retorna quais sao os numeros pares de uma tupla formada por quatro numeros inteiros
    tup(int,int,int,int)->tup'''
	tupla_saida=()
	if numeros[0]%2==0:
		tupla_saida=tupla_saida+(numeros[0],)
	if numeros[1]%2==0:
		tupla_saida=tupla_saida+(numeros[1],)
	if numeros[2]%2==0:
		tupla_saida=tupla_saida+(numeros[2],)
	if numeros[3]%2==0:
		tupla_saida=tupla_saida+(numeros[3],)
		return tupla_saida