def filtra_pares(a):
    """Função que retorna apenas os numeros pares de um tuple com 4 elementos"""
    if type(a)!= tuple or len(a)!=4:
        return ()
    elif a[0]%2=0:
        return a[0]