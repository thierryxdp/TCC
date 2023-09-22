def acima_da_media(lista_notas):
    """ Essa função recebe uma lista com as notas dos alunos
    de uma determinada turma. Posto isso, essa lista retorna-
    rá uma lista ordenada com as notas que ficaram acima da 
    média.
    
    list -> list
    """
    
    
    m = sum(lista_notas)/len(lista_notas)
    lista_ordenada = lista_notas + [m]
    list.sort(lista_ordenada)
    n = list.index(lista_ordenada,m)
    
    if lista_ordenada[n:] is not lista_ordenada[n+1:]:
        nova_lista_ordenada = lista_ordenada[n+1:]
        return nova_lista_ordenada
    
    if lista_ordenada[n:] == lista_ordenada[n+1:]:
        nova_lista_ordenada = lista_ordenada[n+2:]
        return nova_lista_ordenada