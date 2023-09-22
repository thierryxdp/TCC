#Start your python function here
def filtra_pares(conjun):
    '''rece e uma tupla com 4 elementos numericos e retorna
    os elementos pares, conservando a ordem original
    entrada: tuple
    saida: tuple'''
    comp=conjun
    comp_par=()
    if comp[0]%2==0:
        comp_par=comp_par+(comp[0],)
    if comp[1]%2==0:
        comp_par=comp_par+(comp[1],)
    if comp[2]%2==0:
        comp_par=comp_par+(comp[2],)
    if comp[3]%2==0:
        comp_par=comp_par+(comp[3],)
    return comp_par