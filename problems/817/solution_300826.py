def maiores(n_int,n):
    '''Funcao que dada uma lista de numeros e um numero inteiro n, retorna outra lista que contem todos os numeros da lista original maiores que n, ordenados em ordem crescente
str->list,int
saida->list'''
    l_maior=[]
    for k in n_int:
        if k > n:
            l_maior.append(k)
    l_maior.sort()
    return l_maior


def acima_da_media(notas_alunos):
    '''Funcao que retorna a nota dos alunos que ficaram acima da media em ordem crecente
ent->list,int
saida->list'''
    media=sum(notas_alunos)/len(notas_alunos)
    return maiores(notas_alunos,media)