def acima_da_media(notas):
    """Função que recebe uma lista com a as notas dos alunos e retorna a média e a as notas maiores que a média. list -> list"""
    media_notas = sum(notas)/len(notas)
    notas_maiores = []
    for maiores in notas:
        if maiores > media_notas:
            notas_maiores.append(maiores)
    return media_notas, sorted(notas_maiores)