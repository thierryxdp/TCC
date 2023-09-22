def faltante(lista):
    """ Dada uma lista com números diz o número da peça faltante. list -> int """
    
    if (lista[-1]) < len(lista)+1:

        return lista[-1] + 1
    
    if lista[0] == 2:
        return lista[0] -1

    else:

        soma_pa = (len(lista)+1)*((lista[0]+lista[-1])) /2
    
        return int(soma_pa - sum(lista))