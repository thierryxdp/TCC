def filtraMultiplos(lista,n):
    """dada uma lista e um numero n, retorna os
    numeros dessa lista que sao multiplos de n"""
    filtrados=()
    count=0
    while count < len(lista):
        if lista[count]%n==0:
            filtrados=filtrados+(lista[count],)
        count=count+1
        return filtrados