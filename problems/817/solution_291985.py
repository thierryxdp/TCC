def acima_da_media(notaLista):
    """Dada uma lista com as notas de uma turma, retorna apenas
       aquelas com a nota acima da média em ordem ordenada."""
    
    list.sort(notaLista)
    a = sum(notaLista) / 2
    
    return notaLista[notaLista[a]:]