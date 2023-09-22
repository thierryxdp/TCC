def busca(nome,lista):
    """ funcao que recebe uma matriz e faça uma busca por setor, dado um nome um
    numero, a funcao retorna os dados de todos os funcionarios.str-list->list"""

    
    acumulador=[]
    
    for cntt in list(range(len(lista))):
        if nome in lista[cntt]:
            acumulador+=[lista[cntt]]
    return acumulador