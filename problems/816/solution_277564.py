def maiores(int_Lista, int_Num):
    
    lista_Toda = int_Lista.append(int_Num)
    ordenada = int_Lista.sort()
    posicao = lista_Toda.index(int_Num)
    
    return ordenada[posicao+1:]