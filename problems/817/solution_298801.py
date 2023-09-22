def insere(lista,n):
    """essa função dada uma lista ordenada (crescente) de números inteiros (igual ao
parâmetro de entrada lista) e um número inteiro n, inclui n na posição correta, ou
seja, de tal maneira que a lista continue ordenada.
list,int -> list"""
    list.append(lista,n)
    list.sort(lista)
    return lista

def maiores(lista,n):
    """essa função dada uma lista de números inteiros(igual ao parâmetro de entrada
lista) e um número inteiro n, retorna outra lista, que contém todos os números da
lista original maiores que n ordenados em
ordem crescente.
list,int -> list"""
    if n in lista:
        list.sort(lista)
        indice=list.index(lista,n)
        return lista[indice+1:]
    else:
        insere(lista,n)
        indice=list.index(lista,n)
        return lista[indice + 1:]
    
def acima_da_media(notas):
    """essa função, dada uma lista com as notas dos alunos de uma turma(igual ao parâ-
metro de entrada notas), retorna uma lista ordenada com as notas que ficaram acima
da média.
list -> list"""
    num_alunos=len(notas)
    media=(sum(notas)/num_alunos)
    lista= maiores(notas,media)
    return lista