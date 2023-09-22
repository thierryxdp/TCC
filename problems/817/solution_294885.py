def maiores(lista,n):
    '''
    Função que recebe uma lista de números inteiros e um
    número inteiro n e retorna outra lista que contenha 
    todos os números da lista original maiores que n.
    
    list, int -> list
    '''
    if n not in lista:
        lista.append(n)
    lista.sort()
    i=lista.index(n)
    c=lista.count(n)
    return lista[i+c:]

def acima_da_media(notas):
    '''
    Função que recebe uma lista com notas dos alunos de uma
    turma e retorna uma lista ordenada com as notas que
    ficaram acima da média
    
    list -> list
    '''
    media=sum(notas)/len(notas)
    return maiores(notas,media)