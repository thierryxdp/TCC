def maiores (lista,n):

    list.append(lista, n)
   
    list.sort(lista)
    
    return lista[lista.index(n)+1:]
    
def acima_da_media(notas):
    
    """ Função que dada uma listacom as notas dos alunos de uma turma, retorne
	uma lista ordenada com as notas que ficaram acima da média"""
    
    media = sum(notas)/len(notas)
    
    return maiores(notas,media+0.001)