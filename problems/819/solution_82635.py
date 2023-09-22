def filtraMultiplos(lista,n):
    '''Função que recebe uma lista de números inteiros e um número inteiro n e retorna outra lista com contendo todos os elementos da lista original que forem divisíveis por n.
     list[int]->list[int]'''
    multiplos=[]
    indece=0
    while indece<len(lista):
        if lista[indece]%n ==0:
            list.append(multiplos,lista[indece])
        indece=indece+1
    return multiplos