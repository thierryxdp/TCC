def filtra_pares(tupla):
    '''funcao que filtra elementos com 4 parametros e os transforma em pares na mesma ordem em que se encontravam
    int,int,int,int->int,int,int,int'''
    if tupla[0]%2==0:
        return(tupla)
    if tupla[1]%2==0:
        return(tupla)
    if tupla[2]%2==0:
        return(tupla)
    if tupla[3]%2==0:
        return(tupla)
    else:
        return()