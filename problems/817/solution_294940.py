def acima_da_media(notas :list, media :float) -> list:
    """Dada uma lista com as notas dos alunos de uma turma e a
    media da disciplina em questão, retorna uma lista contendo
    as notas que ficaram acima da média."""
    
    list.append(notas,media)
    list.sort(notas)
    acima_med = (list.index[notas,media):]
    list.remove(notas,media)
    
    return acima_med