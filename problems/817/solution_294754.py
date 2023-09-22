def acima_da_media(lista):
    """Função que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média,
    lista --> lista"""
    
    media = sum(lista)/ len(lista)
    
    return maiores(lista,media)