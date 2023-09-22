def qtd_divisores(num):
    lista = []
    for i in range(1, num//2+1):
        if num % i == 0: 
            lista.append(i)
	return f'O número {num} tem {len(lista)+1} divisores.'