def fatorial(n):
    "função que retorna o fatorial de um número"
    "int->int"
    i=1
    fator=1
    extra=n
    while i<n:
        extra=extra*i
        i=i+1
	return extra