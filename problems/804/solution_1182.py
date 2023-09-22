#Start your python function here
def filtra_pares(t):
    """Para retornar apenas os numeros pares de uma tupla, digite;
    tupla-> booleano"""
    if not t:
        return 0            
    return (t[0] % 2 == 0) + filtra_pares(t[1:]