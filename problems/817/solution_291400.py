def acima_da_media (lista):
    """funçao que recebe uma lista com notas de alunos de uma turma e retorna uma lista ordenada com as notas que estao acima da media da turma;
    entrada: list;
    saida: list."""
    media = sum (lista_notas) / len (lista)
    return maiores (lista, media)