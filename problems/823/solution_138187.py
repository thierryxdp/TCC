def faltante(lista):
    """ A função retorna o número de peças
    de quebra cabeça que está faltando
    	list -> int """
    
    i = 1
    x = len(lista) - 1
    
    while i != len(lista) + 2:
        if i not in lista and i < lista[x]:
            return i
        if i not in lista and i > lista[x]:
            return i
        if i in lista:
            i += 1