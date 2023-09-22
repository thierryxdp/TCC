def intercala(lista1, lista2):
    """Escreva duas listas de 3 itens. A funcao retorna uma nova lista, com 6 itens,
    dos elementos da primeira lista intercalados com a segunda.
    #parametros | in: list, list (listas de entrada) -> out: list (lista concatenada)"""
    if len(lista1+lista2)==6:
    	#itens da nova lista:
        a=x[0]
    	b=y[0]
    	c=x[1]
    	d=y[1]
    	e=x[2]
    	f=y[2]
        #uniao dos itens na ordem de saida:
    	intercalado=[a,b,c,d,e,f]
    	return intercalado
	else:
        return 'Digite os valores dentro dos parametros de entrada.'