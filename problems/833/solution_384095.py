def conta_numero(numero,matriz):
    """A funcao retorna quantas vezes um numero dado aparece
	na matriz; int,list-->int"""
    i=0
    qtd=[]
    while i<len(matriz):
        a=matriz[i].count(numero)
    	list.append(qtd,a)
    	i+=1
    return sum(qtd)