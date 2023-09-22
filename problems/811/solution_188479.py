def colchao (medidas,H,L):
    '''Dada os números inteiros das medidas do colchão
       (lista representada por A, B e C), da altura (H)
        e largura (L), retorne true se o colchão passar
        pela porta e false se não passar;
       list, int, int -> bool'''

    ladoA, ladoB, ladoC = medidas [0], medidas [1], medidas [2]
    if ((ladoA<=L and ladoB<=H) or (ladoA <=H and ladoB<=L))or (ladoA<=L and ladoC<=H) or (ladoC<=L and ladoA<=H) or ((ladoC<=L  and  ladoB<=H) or  (ladoB<=L and ladoC<=h)):
        return True
    else:
        return False