#Start your python function here
def filtra_pares(w):
    """funcao que retorna os numeros pares da tupla."""
    resultado=()
    if w[0]%2==0:
        resultado=resultado+(w[0])
    if w[1]%2==0:
        resultado=resultado+(w[1])
    if w[2]%2==0:
        resultado=resultado+(w[2])
    if w[3]%2==0:
        resultado=resultado+(w[3])
    return resultado