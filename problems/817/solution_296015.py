def maiores(lista,n):
    lista2 = [x for x in lista if x > n]
    list.sort(lista2)
    return lista2 

def acima_da_media(lista_notas):
    """Retorna uma lista ordenada com as notas acima da média
	a partir de uma lista com todas as notas dos alunos de uma
    turma.
list -> list"""
    media = sum(lista_notas)/len(lista_notas)
    return maiores(lista_notas,media)

#Casos de teste:
# acima_da_media([4.0,5.5,7.6,2.5,9.0,8.2,3.0]) == [7.6, 8.2, 9.0]
# acima_da_media([3.0,5.0,7,2.2,5.4,6]) == [5.0, 5.4, 6, 7]
# acima_da_media([10,9.2,0.0,2.1,4.5,3.0,2.6,1.5]) == [4.5, 9.2, 10]