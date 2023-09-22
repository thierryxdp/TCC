def maiores(lista,n):
    '''retorna somente os numeros da lista de entrada maiores que n em ordem crescente
       list, int -> list'''
    list.append(lista,n)
    list.sort(lista)
    lista=lista[list.index(lista,n):]
    list.remove(lista,n)
    return lista

def acima_da_media(notas):
    '''função que, dadas as notas dos alunos de uma turma, retorna as notas acima da média
       list -> list'''
    media=sum(notas)/len(notas)
    notas_acima=maiores(notas,media)
    list.remove(notas_acima,media)
    return notas_acima