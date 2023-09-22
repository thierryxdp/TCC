def intercala(lista1,lista2):
    """ A função concatena uma intercalação de termos de uma lista de 3 termos com outra lista de 3 termos;
    list, list -> list """ 
    nullist = []
    lista3 = nullist + [lista1[0],] + [lista2[0],] + [lista1[1],] + [lista2[1],] + [lista1[2],] + [lista2[2],]
    return lista3