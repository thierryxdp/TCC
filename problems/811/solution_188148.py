def colchao(medidas,H,L):
    '''Esta função identifica se o colchão passa por uma porta.
    Instruções: Informe o valor das medidas do colchão dentro de uma lista
    Exemplo ([a,b,c],H,L)
    Medidas do colchão:
    a: Expessura; b: Altura c: Largura'''
#Separando os lados do colchao
	l1 = medidas[1]
    l2 = medidas[2]
#Condições para o colchão passar
	if l1<=L or l2<=L:
       	return l1<=L or l2<=L
	elif l1>L and l2>L:
        return not(l1>L)