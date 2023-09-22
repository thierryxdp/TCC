def insere_sort(sorted_list, n):
    """Faça uma função que dada uma lista ordenada(crescente), inclua n na posição correta"""
    sorted_list.append(n)
    
    sorted_list.sort()

#    return list.sort(sorted_list)
    return sorted_list