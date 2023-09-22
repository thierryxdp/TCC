#Start your python function here
def filtra_pares(a,b,c,d):
    '''recebe uma tupla com 4 elementos numericos e retorna
    os elementos pares, conservando a ordem original
    entrada: tupla
    saida: tupla'''
    comp=(a,b,c,d)
    comp_par=tuple()
    if comp[0]%2==0:
        comp_par=comp_par+(comp[0],)
    if comp[1]%2==0:
        comp_par=comp_par+(comp[1],)
    if comp[2]%2==0:
        comp_par=comp_par+(comp[2],)
    if comp[3]%2==0:
        comp_par=comp_par+(comp[3],)
        return comp_par