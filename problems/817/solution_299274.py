def acima_da_media (lista):
    """dada como entrada uma lsita com as notas de uam turma, a função
    retorna uma lista ordenada com as notas que ficaram acima da média.
    list -> list"""
    
    media = sum(lista)/len(lista)
    
    return media