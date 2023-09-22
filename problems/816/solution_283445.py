def maiores (lista_N_Inteiros, numInt):
    '''Dada uma lista de números inteiros e um outro número
       int n, retorne uma nova lista que contenha todos os da
       lista original maiores que n em ordem crescente;
       list, int -> list'''
    
    novalista = ([i for i in lista_N_Inteiros if i > numInt])
    return sorted(novalista)