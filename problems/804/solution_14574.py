def filtra_pares(x):
    """Dada uma tupla com 4 valores inteiros, retorna esta mesma tupla contendo apenas valores pares. Recebe valores do tipo tuple e retorna um valor do tipo tuple"""
    """Inserir as informações no estilo: filtra_pares([2,4,5,7]) ; filtra_pares([1,12,52,70])"""
    par = ()
    if (x[0])%2 == 0:
        par = par + (x[0],)
    if (x[1])%2 == 0:
        par = par + (x[1],)
    if (x[2])%2 == 0:
        par = par + (x[2],)
    if (x[3])%2 == 0:
        par = par + (x[3],)
    return par