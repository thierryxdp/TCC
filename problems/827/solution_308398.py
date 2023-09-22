def qtd_divisores(x):
	"""Recebe um numero e retorna quantod divisores esse numero possui; int->int."""
	divisores=[]
    n=1
    for x:
        if x % n==0:
            divisores=[n]
        n=+1
    return list.count(divisores)