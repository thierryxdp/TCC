def maiores(int_Lista, int_Num):
    int_Lista.append(int_Num)
    int_Lista.sort()
    posicao = int_Lista.index(int_Num)
    
    return int_lista[posicao+1:]