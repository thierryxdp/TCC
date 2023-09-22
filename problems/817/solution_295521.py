def maiores(lista_numeros, n):
     """ Função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maiores que n;
         list -> list"""
     lista_nova = lista_numeros + [n]
     lista_ordenada = list.sort(lista_nova)
     indice = list.index(lista_nova,n) + 1
     lista_nova = lista_nova[indice: ]
     return lista_nova

def acima_da_media(notas):
    """ Função que dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da média;
        list -> list"""
    lista = list.remove(maiores(notas,5),5)
    return lista