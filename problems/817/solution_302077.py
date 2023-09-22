def acima_da_media(lista):
    """Função que dada as notas dos alunos de uma turma, retorna
    uma lista ordenada com as notas que ficaram acima da média
    Assinatura: list -> list."""
    s = [n for n in lista if n>(sum(lista))/(len(lista))]
    list.sort(s)
    return s