def acima_da_media(lista):
    """Dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada 
    com as notas que ficaram acima da média"""
    """list -> list"""
    
    media = sum(lista)/len(lista)
    
    list.append(lista,media)
    list.sort(lista)
    
    
    
    return lista[list.index(lista,media)+1:len(lista)]