def acima_da_media(*notas):
    """Função dada uma lista com as notas dos alunos de uma turma e retorna uma lista ordenada com as notas que ficaram acima da media
       Parâmetros: list -> list"""
    media_notas = sum(notas)/len(notas)
    maiores_notas = []
    for maiores in notas:
        if maiores > media_notas:
            maiores_notas.append(maiores)
    return media_notas, sorted(maiores_notas)