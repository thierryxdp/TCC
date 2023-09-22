def maiores(lista,n):
    '''Dada uma lista de numeros inteiros e um
    numero inteiro n, retorna outra lista, que contem
    todos os numeros da lista original maiores que n
    list,int->list'''
    lista.append(n)
    lista.sort()
	i = list.index(lista,n)
    return lista[i+1::]
def acima_da_media(notas):
    '''Dada uma lista com as notas dos alunos de uma
    turma, retorna uma lista ordenada com as notas 
    que ficarama acima da media.
    list-> list'''
    qntd = len(notas)
    media = sum(notas)/qntd
    return maiores(notas,media)