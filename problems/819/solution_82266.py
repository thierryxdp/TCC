def filtraMultiplos(listadenumeros,n):
    """Funcao que recebe de entrada uma lista de numeros e um numero n e retorna outra lista contendo todos os numeros divisiveis por n da  lista originial. list, int=>list"""
    multiplos=[]
    x=0
    while x <len (listadenumeros):
        if  listadenumeros[x]%n==0:
            multiplos= multiplos+[listadenumeros[x]]
            x=x+1
    return multiplos