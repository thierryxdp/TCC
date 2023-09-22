def colchao(medidas,H,L):
    ''' Dadas os tamanhos inteiros de A,B E C, a altura 
    da porta e a largura da portal, retorna um valor 
    booleano se o colchao passa ou nao pela porta'''
   	medidas[0] = altura_c
    medidas[1] = grossura_c
    medidas[2] = comprimento_c
    if (altura_c < H) and (grossura_c < L):
        return True
    else:
        return False