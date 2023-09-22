def acima_da_media(notaLista):
    """Dada uma lista com as notas de uma turma, retorna apenas
       aquelas com a nota acima da média em ordem ordenada."""
    
    list.sort(notaLista)
    
    return notaLista[sum(notaLista) / 2:]