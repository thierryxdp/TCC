def filtraMultiplos(lista_orig, num):
    '''função que retorna um lista com os multiplos por um numero num de numeros contidos numa lista lista_orig'''
    '''list, int -> list'''
    multiplos = []
    cont = 0
    while cont < len(lista_orig):
        if lista_orig[cont] % num == 0:
            multiplos.append(lista_orig[cont])
            cont+= 1
        else:
            cont+=1
    return multiplos