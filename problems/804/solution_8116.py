def filtra_pares(n):
    par = ()
''' funcao que retorna numeros pares
int -> tupla
'''
    if n[0] %2==0:
        par =  par + (n[0],)
    if n[1] %2==0:
        par =  par + (n[1],)
    if n[2] %2==0:
        par = par + (n[2],)
    if n[3] %2==0:
        par = par + (n[3],)
        return par