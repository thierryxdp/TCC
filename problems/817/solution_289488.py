def acima_da_media (lista):
    """Função que dada uma lista com notas dos alunos da turma, retorna uma lista ordenada com as notas que ficaram acima da média para aprovação que é igual a 5;
       list -> list."""
    list.sort (lista)
    lista_nova = list.index (lista, 5)
    return lista [lista_nova:]