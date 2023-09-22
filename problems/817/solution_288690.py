def acima_da_media(lista):
    '''acima_da_media recebe uma lista de nota dos alunos de uma turma e devolve uma lista ordenada com as notas que ficaram acima da média.
    list-->list'''
    list.sort(lista)
    z=len(lista)+1
    y=(sum(lista)//z)+1
    n=list.index(lista,y)
   	return lista[n:]