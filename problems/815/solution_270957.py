def insere(lista_numero,n):
    """ funcao que recebe uma lista de numeros e um numero 
    inteiro(n),determina a posicao de n e retorna n dentro da lista em ordem crescente
    list,int->list"""
    lista = lista_numero + [n]
    list.sort(lista)
    return lista