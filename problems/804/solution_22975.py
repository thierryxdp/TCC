def par(x):
    return x%2==0
def filtra_pares(a,b,c,d):
    """ funçao que, com o auxilio da funçao par, verifica quais numeros sao pares e retorna uma tupla contendo eles;
    	int,int,int,int -> tupla(int par, int par, int par, int par);
        exemplo1 -> 2,3,4,5 = (2,4);
        exemplo2 -> 1,3,5,9 = () """
    p = (filtra_pares)
    if  par(p[0]):
        return(p[0])
    elif not par(p[0]):
        not return
    elif par(p[1]):
        return (p[1])
    elif not par(p[1]):
        not return
    elif par(p[2]):
        return (p[2])
    elif not par(p[2]):
        not return
    elif par(p[3]):
        return par(p[3])
    else:
        not return