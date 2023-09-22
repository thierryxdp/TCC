def colchao(medidas,H,L):
    '''Esta função identifica se o colchão passa por uma porta.
    Instruções: Informe o valor das medidas do colchão dentro de uma lista
    Exemplo ([a,b,c],H,L)
    Medidas do colchão:
    a: Expessura; b: Altura c: Largura'''
#Separando os lados do colchao
	l1 = medidas[0]
    l2 = medidas[1]
    l3 = medidas[2]
#Condições para o colchão passar
	if l2<=L or l2<=H or l3<=L or l3<=H:
       	return l2<=L or l2<=H or l3<=L or l3<=H
	else
        return l2<=L or l2<=H or l3<=L or l3<=H