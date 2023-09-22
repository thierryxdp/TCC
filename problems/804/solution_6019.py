'''Função que recebe uma tupla com quatro números inteiros como parâmetro
    e retorna uma nova tupla contendo apenas os elementos pares da tupla original
    na mesma ordem em que se encontravam.
    tupla(int,int,int) -> tupla(int,int,int,int)'''
def filtra_pares(tupla):
    a_par = tupla[0]%2 == 0
    b_par = tupla[1]%2 == 0
    c_par = tupla[2]%2 == 0
    d_par = tupla[3]%2 == 0
    
    if a_par and b_par and c_par and d_par:
        return tuple(tupla)
    elif a_par and b_par and c_par:
        return tuple(tupla[0:3])
    elif a_par and b_par and d_par:
        return tuple(tupla[0:2], tupla[3])
    elif a_par and c_par and d_par:
        return tuple(tupla[0], tupla[2:4])
    elif b_par and c_par and d_par:
        return tuple(tupla[1:4])
    elif a_par and b_par:
        return tuple(tupla[0:2])
    elif a_par and c_par:
        return tuple(tupla[0], tupla[2])
    elif a_par and d_par:
        return tuple(tupla[0], tupla[3])
    elif b_par and c_par:
        return tuple(tupla[1:3])
    elif b_par and d_par:
        return tuple(tupla[1], tupla[3])
    elif c_par and d_par:
        return tuple(tupla[2:4])
    elif a_par:
        return tuple(tupla[0])
    elif b_par:
        return tuple(tupla[1])
    elif c_par:
        return tuple(tupla[2])
    elif d_par:
        return tuple(tupla[3])
    else:
        return 'nenhum número é par.'