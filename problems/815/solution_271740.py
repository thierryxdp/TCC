def insere(lista_numero,n):
    '''Função que recebe de entrada uma lista com numeros 
    inteiros em ordem CRESCENTE e um numero inteiro n 
    qualquer. Retorna n na posição correta da
    ordem crescente.
    list, int -> ????'''
    lista_ordenada = lista_numero + [n]
    list.sort(lista_ordenada)
    return lista_ordenada

#casos de teste
#insere([-500,-890,2,1,45,57],120) == [-890,-500,1,2,45,57,120]
#insere([25,0,21,-98,2],-50) == [-98,-50,0,2,21,25]