def acima_da_media(lista):
    """Dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada 
    com as notas que ficaram acima da média"""
    """list -> list"""
    
    media = sum(lista)/len(lista)
    
    list.sort(lista)
    
    
    return lista[list.index(lista,media)+2:len(lista)]