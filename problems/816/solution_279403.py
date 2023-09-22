def maiores (lista_inteiros,num):
    '''Função que recebe uma lista de numeros inteiros 
    (lista_inteiros) e um numero inteiro qualquer (num)
    e retona todos os numeros maiores que num da lista_inteiros.
    ([list],int) -> list'''

    list.append(lista_inteiros,num)
    list.sort(lista_inteiros)
    posicao=list.index(lista_inteiros,num)
    maiores=lista_inteiros[posicao+1:]

    return maiores