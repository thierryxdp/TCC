def filtra_pares[int1, int2, int3, int4]:
    """Função que irá receber uma tupla com quatro elementos inteiros como parâmetro, e retornar uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam.

        Parameters:
        int1: número inteiro a escolha do usuário
        int2: número inteiro a escolha do usuário
        int3: número inteiro a escolha do usuário
        int4: número inteiro a escolha do usuário
    """
    
	
    if int1%2 == 0 and int2%2 == 0 and int3%2 == 0 and iint4%2 == 0:
        return int1, int2, int3, int4
    elif int1%2 == 0 and int2%2 == 0 and int3%2 == 0:
        return int1, int2, int3
    elif int1%2 == 0 and int2%2 == 0 and int4%2 == 0:
        return int1, int2, int4
    elif int1%2 == 0 and int3%2 == 0 and int4%2 == 0:
        return int1, int3, int4
    elif int2%2 == 0 and int3%2 == 0 and int4%2 == 0:
        return int2, int3, int4
    elif int1%2 == 0 and int2%2 == 0:
        return int1, int2
    elif int1%2 == 0 and int3%2 == 0:
        return int1, int3
    elif int1%2 == 0 and int4%2 == 0:
        return int1, int4
    elif int2%2 == 0 and int3%2 == 0:
        return int2, int3
    elif int2%2 == 0 and int4%2 == 0:
        return int2, int4
    elif int3%2 == 0 and int4%2 == 0:
        return int3, int4
    elif int1%2 == 0:
        return int1
    elif int2%2 == 0:
        return int2
    elif int3%2 == 0:
        return int3
    elif int4%2 == 0:
        return int4
    else:
        return