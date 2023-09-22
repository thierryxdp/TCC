def filtra_pares(tupla):
    '''funcao que filtra elementos com 4 parametros e os transforma em pares na mesma ordem em que se encontravam
    int,int,int,int->int,int,int,int'''
    if tupla[0]%2==0:
        return tupla[0]
    if tupla[1]%2==0:
        return tupla[1]
    if tupla[2]%2==0:
        return tupla[2]
    if tupla[3]%2==0:
        return tupla[3]
    else:
        return()