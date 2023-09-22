def colchao(medidas, H, L):
     A,B,C=medidas
    if H>=L:
        maior_porta= H
        menor_porta= L
    if L>=H:
        maior_porta= L
        menor_porta= H
    if B<=maior_porta and A<= menor_porta:
        return True
    else:
        return False