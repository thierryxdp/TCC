def acima_da_media(lista):
    """" faz a média das notas dos alunos e retorna uma lista daqueles que ficaram acima da média;list->list"""
    o=list.sort(lista)
    m= sum(lista)
    q= m//len(lista)
    return o[q+1:]