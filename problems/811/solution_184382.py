def colchao(medidas,h,l):
    """Função que retorna um valor booleano para saber se um colchão de medidas a, b e c passa pela porta de medidas h e l
       Parametros: list,int,int ->
       Use medidas: ordenada da menor para a maior
       Use h: altura da porta
       Use l: largura da porta"""
    a,b,c = medidas[0],medidas[1],medidas[2]
	menor_lado = min(a,b,c)
	lista_segundo_lado = []
	if menor_lado != a:
	    lista_segundo_lado.append(a)
	elif menor_lado != b:
	    lista_segundo_lado.append(b)
	else:
	    lista_segundo_lado.append(c)
	segundo_lado = min(lista_segundo_lado)
	if menor_lado <= 1 and segundo_lado <= h:
	    return True
	else:
	    return False