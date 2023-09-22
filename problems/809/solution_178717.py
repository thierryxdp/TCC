def intercala(lista1, lista2):
    """Função que dada duas listas (lista1 e lista2), de tamanho 3, gera uma lista3 intercalando elementos as duas listas iniciais;
    <var>, <var> -> <var>"""
    dupla1 = lista1[0],lista2[0]
    dupla2 = lista1[1],lista2[1]
    dupla3 = lista1[2],lista2[2]
    return dupla1+dupla2+dupla3