def fatorial(n):
   #A função irá calcular o fatorial de um número dado pela letra variável n
   #Entrada: int | saída: int
	aux = 1
    i = 1
    while i < n+1:
        aux *= i
		i +=1
    return aux