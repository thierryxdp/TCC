def qtd_divisores(n):
	"""função que retorna a quantidade de divisores do número 
	recebido.
	int -> int"""
    lista = []
    for i in range(1, n+1):
        if n % i == 0:
            resultado = n/i
            lista = resultado
            print(lista)