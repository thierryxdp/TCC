def acima_da_media (lista):
    """Função que dada uma lista com notas dos alunos da turma, retorna uma lista ordenada com as notas que ficaram acima da média;
       list -> list."""
    list.sort (lista)
    lista_nova = sum (lista)/ len (lista)
    return lista [lista_nova:]