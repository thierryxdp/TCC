def maiores (lista, n):
    """funçao que recebe uma lista de numeros inteiros, um numero n e retorna uma lista somente com os numeros maiores que n;
    entrada: list, int
    saida: list."""
    
    if n in lista:
        list.sort (lista)
        ocorrencia = list.index (lista,n)
        return lista [ocorrencia+1:]
    else:
        list.append (lista, n)
        list.sort (lista)
        ocorrencia = list.index (lista,n)
        return lista [ocorrencia+1:]
def acima_da_media (lista):
    """funçao que recebe uma lista com notas de alunos de uma turma e retorna uma lista ordenada com as notas que estao acima da media da turma;
    entrada: list;
    saida: list."""
    media = sum (lista) / len (lista)
    return maiores (lista, media)