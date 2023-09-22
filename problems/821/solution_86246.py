def fatorial(n):
	"""funcao que calcula o fatorial de um numero, int->int"""
    fat=1 
    if int(n)>=1:
        for i in range(1, int(n)+1):
            fat=fat*i
            return "Fatorial de",n,"é:", fat
        else:
            return "Fatorial de "n,"é:", fat