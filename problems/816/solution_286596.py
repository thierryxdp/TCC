def maiores(lista_numeros,n):
    '''Funcao que dada uma lista de numeros inteiros e um
    numero inteiro n, retorna uma segunda lista contendo 
    todos os numeros listados originalmente maiores que n
    em ordem crescente.
    Parametros:
    list,n
	Saida:list
    '''
    l= sorted(lista_numeros + [n])
    h=[]
    for l in l:
        if l >n:
            h.append(l)
    return h