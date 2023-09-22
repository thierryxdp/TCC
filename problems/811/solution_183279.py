def colchao(medidas,H,L):
    '''dada uma lista contendo as três medidas de um colchão, a altura e
    a largura de uma porta, respectivamente, tudo em centímetros, retorna 
    se o colchão passa ou não pela porta;
    list, int, int -> bool'''
    
    A,B,C = medidas
    lado1 = A <= H or A <=L
    lado2 = B <= H or B <= L
    lado3 = C <= H or C <= L
    resultados = str(lado1) + str(lado2) + str(lado3)

    return 2 == str.count(resultados,'True')