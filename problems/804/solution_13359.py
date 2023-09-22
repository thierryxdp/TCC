def filtra_pares(tupla):
    """ Função que recebe uma tupla com quatro elementos inteiros e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam. Caso não tenham elementos pares na tupla, a função retorna uma tupla vazia;
        tuple -> tuple"""
    primeiroe_par = tupla[0]%2==0 
    segundoe_par = tupla[1]%2==0 
    terceiroe_par = tupla[2]%2==0 
    quartoe_par = tupla[3]%2==0 
    if primeiroe_par and segundoe_par and terceiroe_par and quartoe_par:
        return (tupla[0],tupla[1],tupla[2],tupla[3])
    elif primeiroe_par and segundoe_par and terceiroe_par:
        return (tupla[0],tupla[1],tupla[2])
    elif primeiroe_par and segundoe_par and quartoe_par:
        return (tupla[0],tupla[1],tupla[3])
    elif segundoe_par and terceiroe_par and quartoe_par:
        return (tupla[1],tupla[2],tupla[3])
    elif primeiroe_par and terceiroe_par and quartoe_par:
        return (tupla[0],tupla[2],tupla[3])
    elif primeiroe_par and segundoe_par:
        return (tupla[0],tupla[1])
    elif primeiroe_par and terceiroe_par:
        return (tupla[0],tupla[2])
    elif primeiroe_par and quartoe_par:
        return (tupla[0],tupla[3])
    elif segundoe_par and terceiroe_par:
        return (tupla[1],tupla[2])
    elif segundoe_par and quartoe_par:
        return (tupla[1],tupla[3])
    elif terceiroe_par and quartoe_par:
        return (tupla[2],tupla[3])
    elif primeiroe_par:
        return (tupla[0],)
    elif segundoe_par:
        return (tupla[1],)
    elif terceiroe_par:
        return (tupla[2],)
    elif quartoe_par:
        return (tupla[3],)
    else:
        return ()