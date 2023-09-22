def filtraMultiplos(lista,n):
    '''dados uma lista com m elementos, devolve os multiplos de n na mesma ordem de entrada
   tupla -> tupla'''
    pares=()
    proximo=0
    while proximo<len(lista):
        if lista(proximo)%n==0:
            pares=[pares+[lista[proximo]]
        proximo=proximo+1
    return pares