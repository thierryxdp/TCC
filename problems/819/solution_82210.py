def filtraMultiplos(n):
    """funcao que retorna os multiplos de um inteiro n"""
    lista_multiplos=[]
    divisor=1
    while divisor<=n:
        if n%divisor==0:
            lista_multiplos=lista_multiplos + [divisor]
            divisor= divisor+1
    return lista_multiplos