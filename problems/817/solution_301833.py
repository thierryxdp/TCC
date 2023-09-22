def acima_da_media(notas):
    """Função que retorna as nota dos alunos de turma e retorne uma lista
    ordenada com as notas que ficaram acima da media
    assinatura: list -> list"""
    list = []
    media = sum(list)/len(list)
    for nota in notas:
     if nota < media:
        notas.remove(nota)
    return (notas)