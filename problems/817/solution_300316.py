def insere(lista_numero, n):
    '''
    Dada uma lista crescente de números insere o número n na lista de forma que
    ela continue a ser crescente
    
    list, int -> list
    '''
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista_numero, n):
    '''
    recebe uma lista de inteiros lista_numero e um inteiro n e retorna uma lista
    com os inteiros de lista_nuero maiore que n
    
    list, int -> list
    '''
    lista_n=insere(lista_numero, n)
    list.revert(lista_n)
    posicao=list.index(lista_n,n)
    lista_maior=lista_n[:posicao]
    list.revert(lista_maior)
    return lista_maior

def acima_da_media(notas):
    '''
    recebe uma lista de notas e retorna a lista de notas que ficaram acima da média
    de notas dos alunos
    
    list -> list
    '''
	media=sum(notas)/len(notas)
    acima=maiores(notas,media)
    return acima