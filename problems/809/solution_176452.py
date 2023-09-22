def intercala(lista1, lista2):
    '''Função que recebe duas listas de tamanho 3 e retorna uma terceira lista com os elementos de 
    um e dois intercalados
    list, list -> list'''
    lista_soma = lista1 + lista2
    lista3 = lista_soma[0::3] + lista_soma[1::3] + lista_soma[2::3]
    return lista3