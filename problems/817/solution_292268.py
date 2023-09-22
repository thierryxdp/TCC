def acima_da_media(lista):
    """Função que retorna as notas que ficaram acima da média dos alunos de uma turma.List-->List"""
    media = (sum(lista)/len(lista))
    acima = acima_da_media(lista,media)
    return media, acima