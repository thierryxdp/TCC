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
    n=sum(lista)/len(lista)
    if n in lista:
        list.sort(lista)
        acima=list.index(lista,n)
        return lista[acima+1:]
    
    else:
        list.append(lista,n)
        list.sort(lista)
        posicao=list.index(lista,n)
        return lista[posicao+1:]