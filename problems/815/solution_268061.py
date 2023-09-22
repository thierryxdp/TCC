def insere(lista_numero:list,n:int)->list:
    """Função que retorna uma lista ordenanda crescente incluindo um numero N na posição
em que faça a função permanecer ordenada crescente"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero