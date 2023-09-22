def colchao (lista,H, L):
    """funcao que verifica se um colchao de dimensoes A,B e C pode passar por uma porta com altura H e largura L e retorna true em caso positivo e false em caso negativo;
       list, int, int->bool"""
    dim_A=lista[0]
    dim_B=lista[1]
    dim_C=lista[2]
    if (H>dim_C or H==dim_C) and (L>dim_B or L==dim_B):
        return True
    elif (L>dim_A or L==dim_A) and (H>dim_B or H==dim_B):
        return True
    else:
        return False