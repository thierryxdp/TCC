def filtra_pares(x,y,z,w):
    '''Filtra os elementos inteiros pares
    	int,int,int,int-> int'''
    valor=(x,y,z,w)
    if valor%2==0:
        return valor
    else:
        return []