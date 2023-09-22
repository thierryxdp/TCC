def filtra_pares(a):
    """funcao que retorna os termos
       pares do parametro."""

    lista2=()
    for h in a:
        if h %2==0:
            lista2+=(h,)
    return lista2