#Start your python function here
def filtra_pares(lista):
    """Função para filtram os números pares de uma lista com 4 números.
       Onde: "lista" - é uma lista com quatro números.
    lista -> tupla"""
    nova_lista = ( )
    if lista[0] % 2 == 0:
         nova_lista += (lista[0],)
    if lista[1] % 2 == 0:
        nova_lista += (lista[1],)
    if lista[2] % 2 == 0:
        nova_lista += (lista[2],)
    if lista[3] % 2 == 0:
        nova_lista += (lista[3],)
    return nova_lista