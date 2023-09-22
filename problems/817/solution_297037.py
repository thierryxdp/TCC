def maiores(lista,n):
    '''Dados uma lista de números inteiros e um número inteiro,
    retorna uma nova lista com os valores da lista original
    que forem maiores que (n) 
    list, int -> list '''
    a=([i for i in lista if i > n])
    return sorted(a)
def acima_da_media(listanotas):
    '''Dada uma lista com as notas dos alunos de uma turma, 
    retorna uma lista com as notas que ficaram acima da média
    list,int->list'''
    a=sum(listanotas)
    b= len(listanotas)
    c=a/b
    return maiores(listanotas,c)