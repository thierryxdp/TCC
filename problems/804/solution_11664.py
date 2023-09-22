def filtra_pares(tupla):
    """Função que filtra os números pares de uma dada tupla, retornando outra dupla, somente 
com os números selecionados, em ordem em que aparecem; tuple, tuple->tuple"""
    tupla_par = ()
    if tupla[0] % 2 == 0:
        tupla_par = (tupla[0],)
    if tupla[1] % 2 == 0:
        tupla_par = tupla_par + (tupla[1],)
    if tupla[2] % 2 == 0:
        tupla_par = tupla_par + (tupla[2],)
    if tupla[3] % 2 == 0:
        tupla_par = tupla_par + (tupla[3],)
    return tupla_par