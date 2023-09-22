def acima_da_media(lista_notas):
    """função que retorna uma lista com as notas dos alunos que ficaram acima da média,
    através da lista de entrada 'lista_notas';
    Entrada = list
    Saída = list"""
    m = sum(lista_notas)/len(lista_notas)
    
    
    list.append(lista_notas,m)
    list.sort(lista_notas)
    x = list.index(lista_notas,m)
    return lista_notas[x:]