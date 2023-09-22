#Start your python function here
def filtra_pares(numeros):
    """Função que retorna somente os elementos pares de uma 
       tupla original"""
    numerais = ()
    if numeros[0]%2 == 0:
    numerais = numerais + (numeros[0],)
    if numeros[1]%2 == 0:
    numerais = numerais + (numeros[1],)
    if numeros[2]%2 == 0:
    numerais = numerais + (numeros[2],)
    if numeros[3]%2 == 0:
    numerais = numerais + (numeros[3],)
    return numerais