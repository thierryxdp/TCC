def media(*notas):
    """Função que recebe uma lista com a as notas dos alunos e retorna a média e a as notas maiores que a média. list -> list"""
    media_notas = sum(notas[0])/len(notas[0])
    notas_maiores = []
    for maiores in notas[0]:
        if maiores > media_notas:
            notas_maiores.append(maiores)
    return media_notas, sorted(notas_maiores)