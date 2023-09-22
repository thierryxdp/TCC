def intercala(lista1,lista2):
    """funcao que retorna o intercalamento entre as duas listas de tamanho tres;
    list, list -> list"""
    [a,b,c]=lista1
    [x,y,z]=lista2
    return [lista1[0]]+[lista2[0]]+[lista1[1]]+[lista2[1]]+[lista1[2]]+[lista2[2]]