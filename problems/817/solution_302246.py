def maiores (a,n):
    """Função que recebe uma lista de números inteiros e um
    número inteiro n e retorna outra lista que contem todos
    os numeros da lista original maiores que n ordenados em
    ordem crescente
    list, int -> list"""
    list.sort(a)
    lista=[]
    for i in a:
        if i>n:
            lista.append(i)
    return lista

def acima_da_media (l):
    """Função que dada uma lista com as notas dos alunos de uma
    turma, retorna uma lista ordenada com as notas que ficaram 
    acima da média
    list -> list"""
    med= sum(l)/len(l)
    return maiores(l,med)