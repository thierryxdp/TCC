def maiores(lista,n):
    '''
    	Função que recebe como entrada
        uma lista com números inteiros
        e um número inteiro n, e retorna 
        essa lista apenas com os números 
        maiores que n, na ordem crescente
        : param lista: list
        : param n: int
        : return: list
    '''
    list.append(lista,n)
    list.sort(lista)
    indice = list.index(lista,n)
    lista = lista[indice:]
    qtd_n_aparece = list.count(lista,n)
    del lista[0:qtd_n_aparece]
    return lista

def acima_da_media(lista_notas):
    '''
    	Função que recebe uma lista com
        as notas dos alunos de uma turma
        e retorna uma lista ordenada com
        as notas que ficaram acima da
        média
        : param lista_notas: list
        : return: list
    '''
    media = sum(lista_notas)/len(lista_notas)
    return maiores(lista_notas,media)