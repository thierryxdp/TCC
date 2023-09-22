# "Função que tem como objetivo retornar true caso as medidas do colchão passe pelas medidas da porta e false se não passar; list,int,int -> bool"
def intercala(lista1, lista2):
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