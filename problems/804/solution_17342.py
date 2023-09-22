def filtra_pares(t):
    ''' Esta função retorna uma tupla nova apenas com os
elementos paras de uma tupla t.
tuple->tuple'''
    nova_tupla = tuple()
    if (t[0]%2) == 0:
        nova_tupla_par = nova_tupla + (t[0],) 
    elif (t[1]%2) == 0:
        nova_tupla_par = nova_tupla + (t[1],)
    elif (t[2]%2) == 0:
        nova_tupla_par = nova_tupla + (t[2],)
    elif (t[3]%2) == 0:
        nova_tupla_par = nova_tupla + (t[3],)
        return nova_tupla_par