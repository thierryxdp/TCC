def filtra_pares(tupla):
    """Função que recebe uma tupla de quatro valores inteiros e retorna outra
       tupla contendo  apenas os valores pares da tupla original
       parâmetros de entrada: tipo tupla
       parãmetros de saída: tipo tupla"""
    pares=()
    if eh_par(t[0]):
        pares=pares+(t[0],)
    elif eh_par(t[1],):
        pares=pares+(t[1],)
    elif eh_par(t[2]):
        pares=pares+(t[2],)
    elif eh_par(t[3],):
        pares=pares+(t[3],)
    return pares