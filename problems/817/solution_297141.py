def maiores(lista_numero,n):
    """dada uma lista de números inteiros e um número inteiro n, a função retorna uma outra lista que
    contenha todos os números da lista original maiores que n, ordenados em ordem crescente"""
    A=lista_numero
    list.append(A,n)
    list.sort(A)
    B=list.index(A,n)
    A=A[B:]
    return A

def acima_da_media(notas):
    '''dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas que
    ficaram acima da media:
    list-->list'''
    
    media= (sum(notas))/(len(notas))
    
    return maiores(notas,media)