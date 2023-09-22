def acima_da_media(lista):
    """Função que retorna as notas que ficaram acima da média dos alunos de uma turma.List-->List"""
    media = (sum(lista)/len(lista))
    acima = maiores(lista,media)
    return media, acima