def filtraMultiplos(lista_num,n):
    '''Função que dada uma lista de números aleatória (lista_num)
    e um número aleatório (n) retorna uma nova lista com os elementos
    da lista original que são múltiplos de n.
    list[int]->list[int]'''
    
    multiplos=[]
    i=0

    while i < len(lista_num):
        if lista_num[i]%n==0:
            multiplos=multiplos+[lista_num[i]]
        i= i+1

    return multiplos