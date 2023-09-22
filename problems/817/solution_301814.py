def acima_da_media(nota):
    """Função que retorna as nota dos alunos de turma e retorne uma lista
    ordenada com as notas que ficaram acima da media
    assinatura: list -> list"""
    for nota in notas:
    if nota < 5:
        notas.remove(nota)
    return (notas)