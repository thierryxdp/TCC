def colchao(medidas,H,L):
    ''' Dadas os tamanhos inteiros de A,B E C, a altura 
    da porta e a largura da portal, retorna um valor 
    booleano se o colchao passa ou nao pela porta'''
    altura_c = colchao[0][0]
    grossura_c =  colchao[0][1]
	comprimento_c = colchao[0][2]
    if (altura_c < H) and (grossura_c < L):
        return True
    else:
        return False