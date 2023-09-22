def insere(lista_num,n):
    """ Dada uma lista ordenada(crescente), vamos incluir o numero na sua
        posicao correta
        Entrada --> List, Int
        Saida   --> List""" 
    lista = lista_num
    list.insert(lista,-1,n)
    list.sort(lista)
    return lista


""" TESTE
Resultados esperados:
1 - ([1,2,3,4,5,7,8,9],6) ->(1,2,3,4,5,6,7,8,9)
2 - 

Resultados obtidos:
1 - >>> insere([1,2,3,4,5,3,7,8,9],6)
    [1, 2, 3, 3, 4, 5, 6, 7, 8, 9]
"""