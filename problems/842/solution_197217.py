def pontos_por_time (ida, volta, placar):
    """
    funcao que recebe uma lista e retorna um dicionario 
    contendo o nome do time e o numero total de pontos.
    : lista -> dicio
    """
    ida = lista [:1]
    volta = lista [1:]
    placar = ida [2:]
    dicio = { }
    return {placar}