def colchao(medidas,H,L):
    '''Esta função identifica se o colchão passa por uma porta.
    Instruções: Informe o valor das medidas do colchão dentro de uma lista
    Exemplo ([a,b,c],h,l)
    Medidas do colchão:
    a: Expessura; b: Altura c: Largura'''
#Calculo das duas áreas laterais do colchão que podem passar pela porta
	a1 = medidas[0] * medidas[1]
    a2 = medidas[0] * medidas[2]
#Area da porta
	ap = H*L
#Condições para o colchão passar
	if a1<ap or a2<ap:
        return 'K'
    elif a1>=ap and a1>=ap:
        return 'P'