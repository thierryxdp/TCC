def colchao(medidas,H,L):

'''Função que tem como objetivo retornar true caso as medidas do colchão passe pelas medidas da porta e false se não passar; list,int,int -> bool'''

    A,B,C=medidas

    if H>=L:

        menor_porta= H

    if H<=L:

        menor_porta= L

    if B<=maior_porta and A<= menor_porta:

        return True

    else:

        return False