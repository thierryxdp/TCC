def acima_da_media(notas: List[float]):
    """funçao dada as notas de uma turma, retorna a media das notas, e as notas acima da media
    lista-> float , lista"""
    m = sum(notas)/len(notas)
    lista_ordenada = sorted([i for i in notas if i > m])
    return m, lista_ordenada