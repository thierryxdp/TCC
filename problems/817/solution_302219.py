def maiores(lista,n):
    """Função que dada uma lista de n° inteiros e um n inteiro n, retorna outra contendo
    todos os n° da lista original>n, ordenados em ordem crescente;
    list -> list"""
    list.append(lista, n)
    list.sort(lista)
    i = list.index(lista,n)
    return lista[i+1:]

def acima_da_media(notas):
    """Função que dada uma lista com as notas dos alunos de uma turma,retorna outra lista ordenada 
    com as notas acima da media;
    list ->list"""
    media = sum(notas/len(notas))
    n = maiores(notas)
    return n