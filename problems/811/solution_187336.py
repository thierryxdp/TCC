def colchao(lista,h,l):
    """ A função retorna a uma resposta em valor booleano sobre a possibilidade de um colchão
    paralelepípedo passar por uma porta;
    list, int, int -> bool """
    if lista[1] > h and l > lista[1]:
        return True
    elif lista[1] > h:
        return False
    elif lista[0] > h and lista[0] > l:
        return False
    else:
        return True