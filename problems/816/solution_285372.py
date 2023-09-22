def maiores(lista,n):
    """Recebe uma lista com numeros fora de ordem e um numero que é adicionado a lista e devolve outra lista com todos os numeros acima deste numero n;
    	list, int -> list"""
    list.append(lista,n)
    list.sort(lista)
    posicao=list.index(lista,n)
    return lista[posicao:]