def filtra_pares(int1, int2, int3, int4):
    """Função que irá receber uma tupla com quatro elementos inteiros como parâmetro, e retornar uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam.

        Parameters:
        int1: número inteiro a escolha do usuário
        int2: número inteiro a escolha do usuário
        int3: número inteiro a escolha do usuário
        int4: número inteiro a escolha do usuário
    """
    
    int1_par = int1%2 == 0
    int2_par = int2%2 == 0
    int3_par = int3%2 == 0
    int4_par = int4%2 == 0
    
    if int1_par and int2_par and int3_par and int4_par:
        return int1, int2, int3, int4
    elif int1_par and int2_par and int3_par:
        return int1, int2, int3
    elif int1_par and int2_par and int4_par:
        return int1, int2, int4
    elif int1_par and int3_par and int4_par:
        return int1, int3, int4
    elif int2_par and int3_par and int4_par:
        return int2, int3, int4
    elif int1_par and int2_par:
        return int1, int2
    elif int1_par and int3_par:
        return int1, int3
    elif int1_par and int4_par:
        return int1, int4
    elif int2_par and int3_par:
        return int2, int3
    elif int2_par and int4_par:
        return int2, int4
    elif int3_par and int4_par:
        return int3, int4
    elif int1_par:
        return int1
    elif int2_par:
        return int2
    elif int3_par:
        return int3
    elif int4_par:
        return int4
    else:
        return ()