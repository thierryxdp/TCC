#Start your python function here
def filtra_pares(tupla):
    """função que recebe uma tupla com quatro elementos inteiros como 
    parametro, e retorne uma nova tupla contendo apenas os elementos
    pares da tupla original na mesma ordem de contagem
    parametro de entrada:tuple
    valor de saida:tuple
    """
    pares=()
    if tupla[0]%2==0:
        pares= pares+tupla[0]
    if tupla[1]%2==0:
        pares= pares+tupla[1]
    if tupla[2]%2==0:
        pares= pares+tupla[2]
    if tupla[3]%2==0:
        pares= pares+tupla[3]
    
    return pares