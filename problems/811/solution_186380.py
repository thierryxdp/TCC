def colchao(medidas,H,L):
    '''calcula se o colchao passaria pela porta, as medidas do colchao devem ser ordenados em ordem crescente, depois vem altura e largura da porta;
    list[int, int, int], int, int->bool'''
    [A,B,C]= medidas
    if A<=H and B<=L or A<=L and B<=H:
        return True
    else:
        return False