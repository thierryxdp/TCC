def colchao(medidas,h,l):
    '''Função que dado uma lista com as dimensões do colchão em centímetros,
ordenadas da menor para a maior, e dois inteiros H e L, correspondentes respectivamente a altura e a
largura das portas em centímetros, deve retornar se o colchão passa ou não pela porta; list, int, int -> bool'''
    a= lista[0]
    b=lista[1]
    
    if (b<=h and a<=l) or (b<=l and a<=h):
        return True
    else:
        return False