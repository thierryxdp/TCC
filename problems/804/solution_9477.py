def filtra_pares(tupla):
    """ Função que recebe uma tupla com quatro elementos inteiros e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam;
        tuple -> tuple"""
    primeiroe_par = tupla[0]%2==0 and tupla [0]>0
    segundoe_par = tupla[1]%2==0 and tupla [1]>0
    terceiroe_par = tupla[2]%2==0 and tupla [2]>0
    quartoe_par = tupla[3]%2==0 and tupla [3]>0
    if primeiroe_par and segundoe_par and terceiroe_par and quartoe_par:
        return tupla
    elif primeiroe_par and segundoe_par and terceiroe_par:
        return (tupla[0],tupla[1],tupla[2])
    elif primeiroe_par and segundoe_par and quartoe_par:
        return (tupla[0],tupla[1],tupla[3])
    elif segundoe_par and terceiroe_par and quartoe_par:
        return (tupla[1],tupla[2],tupla[3])
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
        return (tupla[0])
    elif segundoe_par:
        return (tupla[1])
    elif terceiroe_par:
        return (tupla[2])
    else:
        return (tupla[3])#Start your python function here