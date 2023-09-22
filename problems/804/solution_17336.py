def filtra_pares(t1, t2, t3, t4):
    ''' Esta função retorna uma tupla nova apenas com os
elementos pares dos números t1, t2, t3 e t4.
int, int, int, int->tuple'''
    nova_tupla = tuple()
    if (t1%2) == 0:
        nova_tupla_par = nova_tupla + (t1,) 
    elif (t2%2) == 0:
        nova_tupla_par = nova_tupla + (t2,)
    elif (t3%2) == 0:
        nova_tupla_par = nova_tupla + (t3,)
    elif (t4%2) == 0:
        nova_tupla_par = nova_tupla + (t4,)
        return nova_tupla_par