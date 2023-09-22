def acima_da_media(notas :list) -> list:
    """Dada uma lista com as notas dos alunos de uma turma e a
    media da disciplina em questão, retorna uma lista contendo
    as notas que ficaram acima da média."""
    
    media = sum(notas) / len(notas)
    
    list.append(notas,media)
    list.sort(notas)
    acima_med = notas[list.index(notas,media):]
    list.remove(acima_med,media)
    
    if acima_med[0] == media:
        del acima_med[0]
        
        return acima_med
    
    else:
        return acima_med