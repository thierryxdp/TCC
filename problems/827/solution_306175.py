def qtd_divisores(n):
    sdn = 0 # a soma dos divisores de n
    for x in range(1,n+1):
        if n%x == 0:
        sdn += x # é a mesma coisa que sdn = sdn +x
    	return sdn # estou usando a versão 3.4 print agora é um função.