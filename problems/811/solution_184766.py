def colchao(medidas,H,L):
    '''Calcula se um x na lista de medidas é menor que os valores da porta
       list,int,int -> bool'''
    for x in medidas[1:]:
        if x < H or x < L:
            return True

        else:
            return False