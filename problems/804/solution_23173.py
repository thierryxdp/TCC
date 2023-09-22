def par(x):
    return x%2 ==0
def filtra_pares(a):
    """ Funçao que, com o auxilido da funçao par, recebe uma tupla contendo 4 numero e retorna uma outra tupla com apenas os numeros pares, se nao houver nenhum, retorna uma tupla vazia;
    	int, int, int, int -> int,int,int,int;
    	exemplo1 -> (3,1,2,6) = (2,6);
        exemplo2 -> (15,11,27,85) = ()"""
    p = ()
    if par(a[0]):
        p = p + (a[0],)
    if par(a[1]):
        p = p + (a[1],)
    if par(a[2]):
        p = p + (a[2],)
    if par(a[3]):
        p = p + (a[3],)
    return p