def filtraMultiplos(lista,n):
    '''dados uma lista com m elementos, devolve os multiplos de n na mesma ordem de entrada
   tupla -> tupla'''
    pares=()
    if lista[0]%n==0:
        pares=pares+(lista[0],)
    if lista[1]%n==0:
        pares=pares+(lista[1],)
    if lista[2]%n==0:
        pares=pares+(lista[2],)
    if lista[3]%n==0:
        pares=pares+(lista[3],)
    return pares