def filtra_pares(numero):
    lista=()
    if numeros[0]%2==0:
        lista=lista+(numero[0],)
    if numeros[1]%2==0:
        lista=lista+(numero[1],)
    if numero[2]%2==0:
        lista=lista+(numero[2],)
    if numero[3]%2==0:
        lista=lista+(numero[3],)
    return lista