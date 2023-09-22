def colchao(medidas,H,L):
'''list,int,int -> bool'''
    A,B,C=medidas
    if H>=L:
        menor_porta= H
    if H<=L:
        menor_porta= L
    if B<=maior_porta and A<= menor_porta:
        return True
    else:
        return False