def qtd_dividores(n):
    i=1
    saida=[]
    while i<n:
        if n//i==0:
            saida.append(i)
        i+=i+1
	return len(saida)