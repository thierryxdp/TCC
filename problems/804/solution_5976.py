def filtra_pares(tupla):
    a_par = tupla[0]%2 == 0
    b_par = tupla[1]%2 == 0
    c_par = tupla[2]%2 == 0
    d_par = tupla[3]%2 == 0
    
    if a_par and b_par and c_par and d_par:
        return tupla[:]
    elif a_par and b_par and c_par:
        return tupla[0:3]
    elif a_par and b_par and d_par:
        return tupla[:]-tupla[2]
    elif a_par and c_par and d_par:
        return tupla[:]-tupla[1]
    elif b_par and c_par and d_par:
        return tupla[:]-tupla[0]
    elif a_par and b_par:
        return tupla[:2]
    elif a_par and c_par:
        return tupla[:3]-tupla[1]
    elif a_par and d_par:
        return tupla[:]-tupla[1:3]
    elif b_par and c_par:
        return tupla[1:3]
    elif b_par and d_par:
        return tupla[1:]-tupla[2]
    elif c_par and d_par:
        return tupla[2:]
    elif a_par:
        return tupla[0]
    elif b_par:
        return tupla[1]
    elif c_par:
        return tupla[2]
    elif d_par:
        return tupla[3]
    else:
        return 'nenhum número é par.'