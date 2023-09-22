def filtra_pares(a):
    '''verifica se os numeros dentro da tupla são pare e os separa em outra tupla'''
    '''tupla (int,int,int,int,...) -> tuple(int,...)'''
    tupla_lista = []
    for pares in a:
        par = True

        if pares % 2 != 0:
            par = False

        if par:
            tupla_lista.append(pares)
    return tuple(tupla_lista)#Start your python function here