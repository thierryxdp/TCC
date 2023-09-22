def filtra_pares(elementos):
    """Função que recebe como entrada uma tupla com quatro elementos inteiros, e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que estavam."""
    resultado = ()
    if elementos[0]%2==0:
        resultado = resultado+(elementos[0],)
    if elementos[1]%2==0:
        resultado = resultado+(elementos[1],)
    if elementos[2]%2==0:
        resultado = resultado+(elementos[2],)
    if elementos[3]%2==0:
        resultado = resultado+(elementos[3],)
    return resultado