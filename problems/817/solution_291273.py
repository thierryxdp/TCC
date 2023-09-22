def acima_da_media(notas):
    """Função que dada uma lista com notas dos alunos de uma turma, retorne uma
    lista ordenada com as notas que ficaram acima da da media.
    Dados de entrada: list.
    Dados de saida: list."""
    soma = sum(notas)
    quantidade = len(notas)
    media = soma/quantidade
    media
    if media in notas:
        return lista[list.index(notas, media) + 1:]