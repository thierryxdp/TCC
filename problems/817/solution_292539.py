def acima_da_media(lista):
    """Função que dada uma lista com as notas dos alunos de uma turma,
       retorna uma lista ordenada com as notas que ficaram acima da média.
       
       Parameters:
       lista: Lista com as notas dos alunos
       
       Returns:
       Retorna uma nova lista ordenada com as notas que ficaram acima da 
       média.
       list -> list
       """
    m=sum(lista)/len(lista)
    if m in lista:
        list.sort(lista)
        acima_m=list.index(lista,m)
        return lista[acima+1:]