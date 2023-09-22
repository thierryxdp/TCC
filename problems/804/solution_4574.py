def filtra_pares(tupla):
    '''Funcao que recebe uma tupla com quatro numeros inteiros e
    retorna uma tupla com somente os numeros pares.
    Entrada: tuple(int, int, int, int)'''
	num1=tupla[0]%2 
    num2=tupla[1]%2  
    num3=tupla[2]%2 
    num4=tupla[3]%2
	n1=tupla[0] 
    n2=tupla[1] 
    n3=tupla[2] 
    n4=tupla[3]
	z=()
	return (n1 if num1%2==0 else z), (n2 if num2%2==0 else z), (n3 if num3%2==0 else z), (n4 if num4%2==0 else z)