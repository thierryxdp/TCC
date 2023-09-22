def contagem(n):
    
    '''Função que dado um número de entrada n, retorna uma lista com todos os inteiros até n. int -> list'''
    
    lista = []
    i = 1
    
    while i <= n:
        lista = lista + [i]
        i = i + 1
    
    return lista

def faltante(listaL):
    
    '''Função que dada uma lista com os números de cada uma das peças de um quebra cabeças, retorna o número da peça faltante. list -> int'''
    
    i = 0
    list.sort(listaL)
    k = listaL[-1]
    listaM = contagem(k)
    listafinal = [sum(listaM) - sum(listaL)]
    
    return listafinal[0]