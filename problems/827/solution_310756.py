def qtd_divisores(n):
	lista = []
	while(x<n):
		if(n % x == 0):
			lista.append(x)
			mult += 1
		x+=1
	else:
		if(mult==0):
            print("É primo.")
		else:
			return lista