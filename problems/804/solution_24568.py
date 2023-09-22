def filtra_pares(elementos):
    """função de recebe uma tupla com quatro elementos inteiros como parâmetro e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam."""
    elementos_pares=()
    if elementos[0]%2==0:
        elementos_pares=elementos_pares+(elementos[0],)
    if elementos[1]%2==0:
        elementos_pares=elementos_pares+(elementos[1],)
    if elementos[2]%2==0:
        elementos_pares=elementos_pares+(elementos[2],)
    if elementos[3]%2==0:
        elementos_pares=elementos_pares+(elementos[3],)
    return elementos_pares