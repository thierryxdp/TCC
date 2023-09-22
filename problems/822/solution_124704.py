def repetitos(lista):
    """Retorna onúmero de vezes que um elemento da lista é
    igual ao elemento anterior;
    list -> int"""
    i=1 #contador
    c=0 #acumulador
    while i < len(lista):
        if lista[i] == lista[i-1]:
            c +=1
        i= 1
    return c