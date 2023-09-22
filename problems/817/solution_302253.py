def maiores (lista,n):
    '''Função de dada uma lista, retorna outra lista coms os nº maiores que n em ordem crescente.
list, int -> list'''
    if n not in lista:
    list.append(lista,n)
    list.sort(lista)
    i = list.index(lista,n) 
    return lista[i+1:]
    else:
    list.sort(lista)
    i = list.index(lista,n) 
    return lista[i+1:]

def acima_da_media (notas):
    '''Função que dada uma lista de notas, retorna outra lista ordenada com as notas dos alunos que estão acima da média.
    list-> list'''
    media = sum(notas)/len(notas)
    return = maiores(notas, media)